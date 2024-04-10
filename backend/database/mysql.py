from contextlib import asynccontextmanager
from sqlalchemy.schema import CreateTable, DropTable
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from models.bulletin import Bulletin
from models.component import Component
from models.course import Course
from models.discussion import Discussion, DiscussionTopic
from models.file import File
from models.notification import Notification
from models.selected_course import SelectedCourse
from models.subscription import Subscription
from models.user import User

Base = declarative_base()

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


async def clear_db():
    async with SessionLocal() as db:
        async with db.begin():
            for table in reversed(Base.metadata.sorted_tables):
                await db.execute(DropTable(table, if_exists=True))

async def init_db():
    async with SessionLocal() as db:
        async with db.begin():
            await db.execute(CreateTable(User.__table__, if_not_exists=True))
            await db.execute(CreateTable(Component.__table__, if_not_exists=True))
            await db.execute(CreateTable(Course.__table__, if_not_exists=True))
            await db.execute(CreateTable(Discussion.__table__, if_not_exists=True))
            await db.execute(CreateTable(DiscussionTopic.__table__, if_not_exists=True))
            await db.execute(CreateTable(File.__table__, if_not_exists=True))
            await db.execute(CreateTable(Notification.__table__, if_not_exists=True))
            await db.execute(CreateTable(SelectedCourse.__table__, if_not_exists=True))
            await db.execute(CreateTable(Subscription.__table__, if_not_exists=True))
            await db.execute(CreateTable(Bulletin.__table__, if_not_exists=True))
            
            
            
async def close_db():
    async with SessionLocal() as db:
        async with db.begin():
            await db.execute(DropTable(Bulletin.__table__))
            await db.execute(DropTable(Subscription.__table__))
            await db.execute(DropTable(SelectedCourse.__table__))
            await db.execute(DropTable(Notification.__table__))
            await db.execute(DropTable(File.__table__))
            await db.execute(DropTable(DiscussionTopic.__table__))
            await db.execute(DropTable(Discussion.__table__))
            await db.execute(DropTable(Course.__table__))
            await db.execute(DropTable(Component.__table__))
            await db.execute(DropTable(User.__table__))
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
