from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import CreateTable

from models.user import User
from models.course import Course
from models.course_bulletin import Course_bulletin
from models.discussion import Discussion
from models.discussion_topic import Discussion_topic

engine = create_async_engine(
    url="mysql+aiomysql://root:password@localhost:8888/yego",
    echo=True,
    pool_pre_ping=True
)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, autocommit=False)


@asynccontextmanager
async def get_db():
    async with SessionLocal() as db:
        async with db.begin():
            yield db


async def init_db():
    async with SessionLocal() as db:
        async with db.begin():
            await db.execute(CreateTable(User.__table__, if_not_exists=True))
            await db.execute(CreateTable(Course.__table__, if_not_exists=True))
            await db.execute(CreateTable(Course_bulletin.__table__, if_not_exists=True))
            await db.execute(CreateTable(Discussion.__table__, if_not_exists=True))
            await db.execute(CreateTable(Discussion_topic.__table__, if_not_exists=True))


async def close_db():
    await engine.dispose()


def db_session_decorator(func):
    async def wrapper(*args, **kwargs):
        async with get_db() as db_session:
            kwargs["db_session"] = db_session
            result = await func(*args, **kwargs)
            return result
        
    return wrapper


def crud_class_decorator(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            setattr(cls, name, db_session_decorator(method))

    return cls
