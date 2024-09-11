from app.initial_data import create_superuser

from .db.config import init_db


async def startup() -> None:
    await init_db()
    await create_superuser()
