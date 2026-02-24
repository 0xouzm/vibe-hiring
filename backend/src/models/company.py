"""Company-related Pydantic models."""

from pydantic import BaseModel, EmailStr


class CompanyCreate(BaseModel):
    """Request body for creating a new company profile."""

    name: str
    industry: str
    size: str


class CompanyResponse(BaseModel):
    """Public company representation returned by the API."""

    id: str
    name: str
    industry: str
    size: str
    cas_score: float | None = None
    cas_tier: str | None = None


class InviteRequest(BaseModel):
    """Request body for inviting an employee to fill the Company DNA survey."""

    email: EmailStr
    name: str


class CASResponse(BaseModel):
    """Culture Authenticity Score breakdown for a company."""

    company_id: str
    score: float
    tier: str
    internal_consistency: float
    hr_employee_alignment: float
