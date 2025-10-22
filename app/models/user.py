"""User model"""
from pydantic import BaseModel


class User(BaseModel):
    """User model for REST API"""
    id: int
    name: str
    email: str
