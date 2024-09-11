import motor.motor_asyncio
from beanie import init_beanie

from app.core.config import settings


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URI)
    await init_beanie(
        database=client.db_name, document_models=["app.users.models.User"]
    )
