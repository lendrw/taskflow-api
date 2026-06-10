from datetime import datetime, UTC

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from app.core.database import check_database_connection
from app.schemas.common import ObjectIdStr
from app.schemas.pagination import PaginationParams

app = FastAPI(
    title="TaskFlow API",
    version="1.0.0",
)


class TestPayload(BaseModel):
    name: str = Field(..., min_length=3)
    email: str


@app.get("/")
def root():
    return {"message": "TaskFlow API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-check")
async def db_check():
    is_connected = await check_database_connection()

    if not is_connected:
        raise HTTPException(
            status_code=500,
            detail="Database connection failed",
        )

    return {"database": "connected"}


@app.get("/test-object-id/{item_id}")
def test_object_id(item_id: ObjectIdStr):
    return {"id": item_id}


@app.get("/test-pagination")
def test_pagination(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
):
    params = PaginationParams(page=page, limit=limit)

    return {
        "data": [],
        "page": params.page,
        "limit": params.limit,
        "total": 0,
        "total_pages": 0,
    }


@app.post("/test-required-fields")
def test_required_fields(payload: TestPayload):
    return {
        "message": "Payload valid",
        "data": payload,
        "created_at": datetime.now(UTC),
    }
