"""Main FastAPI application with REST endpoints"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import users, posts

app = FastAPI(title="REST to GraphQL Migration API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include REST API routers
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(posts.router, prefix="/api", tags=["posts"])


@app.get("/")
def root():
    return {"message": "REST API - Ready for GraphQL migration"}


@app.get("/health")
def health():
    return {"status": "healthy"}
