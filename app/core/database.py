from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.core.config import settings


client = AsyncIOMotorClient(settings.mongo_uri)


def get_database() -> AsyncIOMotorDatabase:
    return client[settings.mongo_db]


async def check_database_connection() -> bool:
    try:
        await client.admin.command("ping")
        return True
    except Exception:
        return False
