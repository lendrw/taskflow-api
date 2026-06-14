from fastapi import APIRouter, HTTPException, status

from app.schemas.auth import RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest):
    try:
        return await AuthService.register(payload)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )
