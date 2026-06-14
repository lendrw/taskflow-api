from bson import ObjectId
from app.core.database import get_database


class UserRepository:
    @staticmethod
    async def find_by_email(email: str):
        db = get_database()
        return await db.users.find_one(
            {
                "email": email,
                "deleted_at": None,
            }
        )

    @staticmethod
    async def create(user_data: dict):
        db = get_database()

        result = await db.users.insert_one(user_data)

        return await db.users.find_one(
            {
                "_id": result.inserted_id,
            }
        )

    @staticmethod
    async def count_users():
        db = get_database()

        return await db.users.count_documents(
            {
                "deleted_at": None,
            }
        )
