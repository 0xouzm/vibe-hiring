from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from loguru import logger

from src.core.config import settings
from src.core.deps import close_db, init_db
from src.core.logging import setup_logging
from src.core.middleware import setup_middleware
from src.models.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("Starting TalentDrop backend")

    # Ensure data directory exists
    db_path = Path(settings.database_url)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Initialize database
    db = await init_db(settings.database_url)
    await create_tables(db)
    logger.info("Database initialized")

    yield

    await close_db()
    logger.info("TalentDrop backend stopped")


app = FastAPI(
    title="知遇 API",
    description="AI 驱动的深度人才匹配平台",
    version="0.2.0",
    lifespan=lifespan,
)

setup_middleware(app)

# Register routers
from src.api.auth import router as auth_router
from src.api.answers import router as answers_router
from src.api.chat import router as chat_router
from src.api.company import router as company_router
from src.api.graph import router as graph_router
from src.api.drop import router as drop_router
from src.api.matching import router as matching_router
from src.api.profile import router as profile_router
from src.api.questions import router as questions_router
from src.api.resume import router as resume_router
from src.api.roles import router as roles_router
from src.api.scores import router as scores_router

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(questions_router, prefix="/api/questions", tags=["questions"])
app.include_router(answers_router, prefix="/api/answers", tags=["answers"])
app.include_router(scores_router, prefix="/api/scores", tags=["scores"])
app.include_router(company_router, prefix="/api/companies", tags=["companies"])
app.include_router(matching_router, prefix="/api/matching", tags=["matching"])
app.include_router(matching_router, prefix="/api/matches", tags=["matches"])
app.include_router(drop_router, prefix="/api", tags=["drops"])
app.include_router(roles_router, prefix="/api/roles", tags=["roles"])
app.include_router(profile_router, prefix="/api/profile", tags=["profile"])
app.include_router(chat_router, prefix="/api/chat", tags=["chat"])
app.include_router(resume_router, prefix="/api/resume", tags=["resume"])
app.include_router(graph_router, prefix="/api/graph", tags=["graph"])


@app.get("/api/health")
async def health():
    return {"status": "ok"}
