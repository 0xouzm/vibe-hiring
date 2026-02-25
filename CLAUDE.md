# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TalentDrop (知遇) is an AI-powered talent matching platform inspired by Date Drop's deep-matching algorithm. Instead of endless job applications, both candidates and companies complete deep questionnaires (Career DNA / Company DNA), and the algorithm "drops" matched opportunities weekly. Currently in the **concept + prototype stage** — product design docs and a static HTML prototype are complete; no application code has been implemented yet.

## Repository Structure

- `prototype/` — Static HTML/CSS/JS interactive prototype (single `index.html`, viewable in browser)
- `discuss/` — Product design, brainstorming, and review documents (Chinese)
  - `brainstorm.md` — Core product concept: 6 mechanisms, user journeys, business model
  - `anti-gaming-mechanism.md` — 7-layer anti-cheating design for the questionnaire system
  - `question-bank-design.md` — Question design methodology (psychometrics + game theory)
  - `question-bank-full.md` — Complete 30-question standardized behavioral assessment bank
  - `matching-architecture.md` — 3-layer matching engine architecture (LightRAG + algorithms + evolution)
  - `matching-algorithm-research.md` — Industry research: Eightfold, Pymetrics, Hinge, OkCupid, CMB, etc.
  - `pitch-theoretical-foundation.md` — **[Pitch Deck]** Theoretical foundation & academic references for Career DNA
  - `company-dna-design.md` — Company DNA questionnaire design: aggregation algorithm, Culture Authenticity Score
  - `company-dna-full.md` — Complete 20-question Company DNA behavioral assessment bank
  - `demo-phase1-gap-analysis.md` — Demo Phase 1 gap analysis with prioritized execution plan
  - `demo-dataset.md` — Demo dataset: 3 fictional companies + 6 candidates + match matrix + sample reports

## Key Product Concepts

- **Career DNA**: 50+ dimension deep profile. 8 core dimensions (Pace, Collab, Decision, Expression, Unc, Growth, Motiv, Execution), all spectrums with no "right answer"
- **Weekly Drop**: Tuesday 9PM curated match reveal with compatibility reports
- **Three-layer question architecture**: Platform standard (30q, 60%) → Job-type specific (15q, 25%) → Company custom (≤5q, 15%)
- **Anti-gaming**: Behavioral scenarios, forced rankings, cross-validation across 4-5 questions per dimension, consistency scoring

## Living Documents

The following documents must be maintained in sync with development and product iterations:

- **`discuss/pitch-theoretical-foundation.md`** — Pitch deck material with academic backing for Career DNA dimensions. Update whenever:
  - A Career DNA dimension is added, removed, or redefined
  - New academic references are discovered or cited
  - Validity/reliability data becomes available
  - Matching algorithm changes affect theoretical framing
- **`discuss/matching-architecture.md`** — Core matching engine architecture. Update whenever:
  - Algorithm layers are implemented or modified
  - Tech stack decisions are finalized
  - Evolution mechanisms are tuned with real data

## Design System (from prototype)

- **Colors**: Midnight `#070b1a`, Indigo `#6366f1`, Coral `#ff6b4a`, Amber `#f59e0b`, Emerald `#10b981`
- **Typography**: Syne (display) + DM Sans (body)
- **Style**: Dark theme, glassmorphism cards, frosted glass overlays

## When Implementation Begins

The global CLAUDE.md mandates these constraints for any code written:

- **Framework**: Next.js v15.3+ with React v19+, Tailwind CSS v4, TypeScript (ESM only, no CommonJS)
- **File limits**: ≤300 lines per file (JS/TS), ≤8 files per directory level
- **Strong typing**: All data structures must be typed; no `any` without explicit approval
- **Docs**: Chinese markdown in `docs/` (formal) and `discuss/` (drafts); all UI text in Chinese
- **Scripts**: Maintain run/debug shell scripts in `scripts/`
- **Logging**: Configure file output to `logs/`
- **Python** (if used for matching algorithm): Use `uv` exclusively, virtualenv as `.venv`
