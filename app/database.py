from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings




engine = create_async_engine(settings.DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# # Во 2.0 версии Алхимии был добавлен async_sessionamaker.
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
class Base(DeclarativeBase):
    pass





