"""REST API endpoints for posts - to be migrated to GraphQL"""
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# Mock database
fake_posts_db = [
    {"id": 1, "title": "First Post", "content": "Hello World", "author_id": 1},
    {"id": 2, "title": "Second Post", "content": "GraphQL is cool", "author_id": 2},
]


@router.get("/posts", response_model=List[dict])
def get_posts():
    """Get all posts - REST endpoint"""
    return fake_posts_db


@router.get("/posts/{post_id}", response_model=dict)
def get_post(post_id: int):
    """Get post by ID - REST endpoint"""
    post = next((p for p in fake_posts_db if p["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/posts", response_model=dict)
def create_post(title: str, content: str, author_id: int):
    """Create new post - REST endpoint"""
    new_id = max([p["id"] for p in fake_posts_db]) + 1 if fake_posts_db else 1
    new_post = {"id": new_id, "title": title, "content": content, "author_id": author_id}
    fake_posts_db.append(new_post)
    return new_post
