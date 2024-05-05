from sqlalchemy import select
from base import async_session_factory
from base import async_engine, Base, async_session_factory
from models import UsersOrm
from sqlalchemy.ext.asyncio import AsyncSession
from dto import User

# from models import NotesOrm


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Initialized the db")


async def all_users(session: AsyncSession):
    query = select(UsersOrm)
    result = await session.execute(query)
    users = result.all()
    print(users)