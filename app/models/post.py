"""Post model"""
from pydantic import BaseModel


class Post(BaseModel):
    """Post model for REST API"""
    id: int
    title: str
    content: str
    author_id: int
