from fastapi import FastAPI, HTTPException

from app.core.database import check_database_connection

app = FastAPI(
    title="TaskFlow API",
    version="1.0.0",
)


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
