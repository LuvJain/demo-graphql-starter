"""REST API endpoints for users - to be migrated to GraphQL"""
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User

router = APIRouter()

# Mock database
fake_users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]


@router.get("/users", response_model=List[dict])
def get_users():
    """Get all users - REST endpoint"""
    return fake_users_db


@router.get("/users/{user_id}", response_model=dict)
def get_user(user_id: int):
    """Get user by ID - REST endpoint"""
    user = next((u for u in fake_users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=dict)
def create_user(name: str, email: str):
    """Create new user - REST endpoint"""
    new_id = max([u["id"] for u in fake_users_db]) + 1 if fake_users_db else 1
    new_user = {"id": new_id, "name": name, "email": email}
    fake_users_db.append(new_user)
    return new_user
