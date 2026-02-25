"""Role (open position) Pydantic models."""

from pydantic import BaseModel


class SalaryRange(BaseModel):
    """Salary range for a role."""

    min: int
    max: int
    currency: str = "USD"


class RoleCreate(BaseModel):
    """Request body for creating a new role."""

    title: str
    level: str | None = None
    skills: list[str] = []
    nice_to_have: list[str] = []
    salary_range: SalaryRange | None = None
    location: str | None = None
    remote_policy: str | None = None  # remote / hybrid / onsite
    description: str | None = None


class RoleUpdate(BaseModel):
    """Request body for updating an existing role."""

    title: str | None = None
    level: str | None = None
    skills: list[str] | None = None
    nice_to_have: list[str] | None = None
    salary_range: SalaryRange | None = None
    location: str | None = None
    remote_policy: str | None = None
    description: str | None = None
    is_active: bool | None = None


class RoleResponse(BaseModel):
    """Public representation of an open role."""

    id: str
    company_id: str
    company_name: str = ""
    title: str
    level: str | None = None
    skills: list[str] = []
    nice_to_have: list[str] = []
    salary_range: SalaryRange | None = None
    location: str | None = None
    remote_policy: str | None = None
    description: str | None = None
    is_active: bool = True
    created_at: str
