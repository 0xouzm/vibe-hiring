"""Question bank routes — serve Career DNA and Company DNA questions."""

from fastapi import APIRouter

from src.models.questionnaire import Question
from src.data.career_questions import CAREER_QUESTIONS
from src.data.company_questions import COMPANY_QUESTIONS

router = APIRouter()


@router.get("/career-dna", response_model=list[Question])
async def get_career_dna_questions():
    """Return the full 30-question Career DNA questionnaire."""
    return CAREER_QUESTIONS


@router.get("/company-dna", response_model=list[Question])
async def get_company_dna_questions():
    """Return the full 20-question Company DNA questionnaire."""
    return COMPANY_QUESTIONS
