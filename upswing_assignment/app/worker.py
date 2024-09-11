from pydantic.utils import import_string
from saq import Queue

from .core.config import settings
from .db.config import init_db

BACKGROUND_FUNCTIONS = [
    "app.users.tasks.log_user_email",
    "app.services.email.send_email_task",
]
FUNCTIONS = [import_string(bg_func) for bg_func in BACKGROUND_FUNCTIONS]


async def startup(_: dict):
    """
    Binds a connection set to the db object.
    """

    await init_db()


queue = Queue.from_url(settings.REDIS_URL)

settings = {
    "queue": queue,
    "functions": FUNCTIONS,
    "concurrency": 10,
    "startup": startup,
    # "shutdown": shutdown,
}
