from datetime import datetime
from pydantic import BaseModel, Field


class TimestampSchema(BaseModel):
    created_at: datetime = Field(..., examples=["2026-06-10T18:30:00"])
    updated_at: datetime | None = Field(None, examples=["2026-06-10T18:40:00"])
    deleted_at: datetime | None = Field(None, examples=[None])
