from pydantic import BaseModel, EmailStr
from typing import Optional


# ── Auth Schemas ──

class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    career_goal: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    career_goal: Optional[str] = None
    resume_ats_score: Optional[int] = None
    github_score: Optional[int] = None
    linkedin_score: Optional[int] = None
    github_username: Optional[str] = None

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserOut


class MessageResponse(BaseModel):
    message: str