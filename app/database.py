from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DR_HOST='localhost'
DR_PORT= 5432
DR_USER='postgres'
DR_PASS='postgres'
DR_NAME='postgres'

DATABASE_URL = f"postgresql+asyncpg://{DR_USER}:{DR_PASS}@{DR_HOST}:{DR_PORT}/{DR_NAME}"

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# # Во 2.0 версии Алхимии был добавлен async_sessionamaker.
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
class Base(DeclarativeBase):
    pass





