"""Tasks for the Async scheduler to run"""
from ottbot.core.db import AsyncPGDatabase
import datetime


async def clean_invite_table(db: AsyncPGDatabase) -> None:
    """Clean the invite table of invites that are no longer valid"""
    await db.execute("DELETE FROM invites WHERE expires_at < $1 AND uses = 0", datetime.datetime.utcnow(tz=datetime.timezone.utc))
