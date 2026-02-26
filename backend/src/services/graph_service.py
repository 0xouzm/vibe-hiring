"""Knowledge graph service — build graph data for visualization."""

import json

import aiosqlite


async def build_candidate_graph(
    db: aiosqlite.Connection,
    candidate_id: str,
) -> dict:
    """Build a knowledge graph for a candidate's profile.

    Returns nodes and edges for force-directed graph visualization.
    """
    nodes: list[dict] = []
    edges: list[dict] = []

    # Central candidate node
    cursor = await db.execute(
        "SELECT name FROM users WHERE id = ?", (candidate_id,)
    )
    user = await cursor.fetchone()
    if not user:
        return {"nodes": [], "edges": []}

    name = user["name"]
    nodes.append({"id": candidate_id, "label": name, "type": "person", "size": 40})

    # DNA dimensions
    cursor = await db.execute(
        "SELECT scores FROM dna_scores WHERE entity_id = ? AND entity_type = 'candidate'",
        (candidate_id,),
    )
    dna_row = await cursor.fetchone()
    if dna_row:
        scores = json.loads(dna_row["scores"])
        dim_labels = {
            "pace": "工作节奏", "collab": "协作模式", "decision": "决策风格",
            "expression": "表达风格", "unc": "不确定性", "growth": "成长路径",
            "motiv": "驱动力", "execution": "执行风格",
        }
        for dim, label in dim_labels.items():
            val = scores.get(dim, 50)
            node_id = f"dim-{dim}"
            nodes.append({
                "id": node_id, "label": f"{label}: {val}",
                "type": "dimension", "size": 15 + val * 0.2,
            })
            edges.append({
                "source": candidate_id, "target": node_id,
                "weight": val / 100,
            })

    # Profile skills
    cursor = await db.execute(
        "SELECT skills FROM user_profiles WHERE user_id = ?", (candidate_id,)
    )
    prof_row = await cursor.fetchone()
    if prof_row and prof_row["skills"]:
        skills = json.loads(prof_row["skills"])
        for skill in skills[:10]:
            skill_id = f"skill-{skill.lower().replace(' ', '-')}"
            nodes.append({"id": skill_id, "label": skill, "type": "skill", "size": 20})
            edges.append({
                "source": candidate_id, "target": skill_id, "weight": 0.6,
            })

    return {"nodes": nodes, "edges": edges}


async def build_match_graph(
    db: aiosqlite.Connection,
    match_id: str,
) -> dict:
    """Build a merged knowledge graph for a match — both candidate and company."""
    cursor = await db.execute(
        "SELECT candidate_id, company_id, role_id, dimension_scores FROM matches WHERE id = ?",
        (match_id,),
    )
    match = await cursor.fetchone()
    if not match:
        return {"nodes": [], "edges": []}

    candidate_id = match["candidate_id"]
    company_id = match["company_id"]
    role_id = match["role_id"]

    # Build candidate side
    candidate_graph = await build_candidate_graph(db, candidate_id)

    # Build company side
    company_nodes, company_edges = await _build_company_nodes(
        db, company_id, role_id,
    )

    # Build match connections (dimension compatibility edges)
    match_edges = _build_match_edges(
        match["dimension_scores"], candidate_id, company_id,
    )

    all_nodes = candidate_graph["nodes"] + company_nodes
    all_edges = candidate_graph["edges"] + company_edges + match_edges

    return {"nodes": all_nodes, "edges": all_edges}


async def _build_company_nodes(
    db: aiosqlite.Connection,
    company_id: str,
    role_id: str | None,
) -> tuple[list[dict], list[dict]]:
    """Build nodes and edges for a company."""
    nodes: list[dict] = []
    edges: list[dict] = []

    cursor = await db.execute(
        "SELECT name FROM companies WHERE id = ?", (company_id,)
    )
    comp = await cursor.fetchone()
    if not comp:
        return nodes, edges

    nodes.append({
        "id": company_id, "label": comp["name"],
        "type": "company", "size": 40,
    })

    # Role node
    if role_id:
        cursor = await db.execute(
            "SELECT title, skills FROM roles WHERE id = ?", (role_id,)
        )
        role = await cursor.fetchone()
        if role:
            nodes.append({
                "id": role_id, "label": role["title"],
                "type": "role", "size": 25,
            })
            edges.append({
                "source": company_id, "target": role_id, "weight": 0.8,
            })
            # Role skills
            if role["skills"]:
                for skill in json.loads(role["skills"])[:6]:
                    skill_id = f"req-{skill.lower().replace(' ', '-')}"
                    nodes.append({
                        "id": skill_id, "label": skill,
                        "type": "requirement", "size": 18,
                    })
                    edges.append({
                        "source": role_id, "target": skill_id, "weight": 0.5,
                    })

    return nodes, edges


def _build_match_edges(
    dimension_scores_json: str,
    candidate_id: str,
    company_id: str,
) -> list[dict]:
    """Create edges connecting candidate and company clusters."""
    edges: list[dict] = []

    # Direct link between candidate and company
    edges.append({
        "source": candidate_id,
        "target": company_id,
        "weight": 0.5,
        "type": "match",
    })

    try:
        scores = json.loads(dimension_scores_json) if dimension_scores_json else {}
    except (json.JSONDecodeError, TypeError):
        return edges

    # High-compatibility dimensions link to company
    for dim, val in scores.items():
        compat = float(val) / 100.0
        if compat > 0.6:
            edges.append({
                "source": f"dim-{dim}",
                "target": company_id,
                "weight": compat * 0.4,
                "type": "match",
            })

    return edges
