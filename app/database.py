from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DR_HOST='localhost'
DR_PORT=5432
DR_USER='postgres'
DR_PASS='postgres'
DR_NAME='postgres'

DATABAE_URL = f"postgresql+asyncpg2://{DR_USER}:{DR_PASS}@{DR_HOST}/{DR_PORT}"

engine = create_async_engine(DATABAE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass