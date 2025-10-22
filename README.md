# REST to GraphQL Migration Starter

FastAPI application with working REST endpoints, ready to be migrated to GraphQL.

## Structure

```
app/
├── main.py              # FastAPI app with REST routers
├── api/
│   ├── users.py         # REST /users endpoints
│   └── posts.py         # REST /posts endpoints
└── models/
    ├── user.py          # User model
    └── post.py          # Post model

frontend/
└── src/
    └── api/
        └── client.ts    # REST API client (fetch-based)
```

## What's Missing (To Be Implemented)

- `strawberry-graphql` Python package
- `@apollo/client` npm package
- `app/graphql/schema.py` - GraphQL schema
- `app/graphql/types/` - GraphQL types (User, Post)
- `app/graphql/resolvers/` - GraphQL resolvers
- Updated frontend client using Apollo Client

## Current Endpoints (REST)

- `GET /api/users` - Get all users
- `GET /api/users/{id}` - Get user by ID
- `POST /api/users` - Create user
- `GET /api/posts` - Get all posts
- `GET /api/posts/{id}` - Get post by ID
- `POST /api/posts` - Create post

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs for API documentation
