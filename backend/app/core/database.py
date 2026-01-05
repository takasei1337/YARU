from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# Create Async Engine
# echo=True allows seeing SQL queries in logs (good for debugging, disable in prod)
engine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    echo=True,
    future=True
)

# Create Async Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

# Base class for models
class Base(DeclarativeBase):
    pass

# Dependency for FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
