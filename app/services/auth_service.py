from datetime import UTC, datetime

from app.core.security import hash_password
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest


class AuthService:
    @staticmethod
    async def register(payload: RegisterRequest):
        existing_user = await UserRepository.find_by_email(payload.email)

        if existing_user:
            raise ValueError("Email already registered")

        total_users = await UserRepository.count_users()
        role = "ADMIN" if total_users == 0 else "MEMBER"

        now = datetime.now(UTC)

        user_data = {
            "name": payload.name,
            "email": payload.email,
            "password_hash": hash_password(payload.password),
            "role": role,
            "created_at": now,
            "updated_at": now,
            "deleted_at": None,
        }

        user = await UserRepository.create(user_data)

        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "created_at": user["created_at"],
            "updated_at": user["updated_at"],
        }
