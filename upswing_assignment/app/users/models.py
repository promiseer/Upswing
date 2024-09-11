from __future__ import annotations

from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase


class User(BeanieBaseUser[PydanticObjectId]):
    short_name: str | None = None
    full_name: str | None = None

    def __str__(self):
        return self.short_name or self.full_name or self.email


async def get_user_db():
    yield BeanieUserDatabase(User)
