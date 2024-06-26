import os
from contextlib import asynccontextmanager
from sqlalchemy.schema import CreateTable, DropTable
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from database.gen_fakeDB import GenFakeDB
from database.init_db import FakeDB
from models.bulletin import Bulletin
from models.component import Component
from models.course import Course
from models.discussion import Discussion, DiscussionTopic, DiscussionTopicReply
from models.file import File
from models.notification import Notification
from models.selected_course import SelectedCourse
from models.group import Group
from models.subscription import Subscription
from models.user import User
from models.report import Report, ReportReply
from models.course_material import CourseMaterial, MaterialInfo, Assignment

engine = create_async_engine(
    url="mysql+aiomysql://root:password@localhost:8888/yego",
    echo=True,
    pool_pre_ping=True
)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, autocommit=False)
gen_fake_db = GenFakeDB()

@asynccontextmanager
async def get_db():
    async with SessionLocal() as db:
        async with db.begin():
            yield db


async def init_db():
    async with SessionLocal() as db:
        # gen_fake_db.generate()
        gen_fake_db.demo()

        async with db.begin():
            await db.execute(CreateTable(User.__table__, if_not_exists=True))
            await db.execute(CreateTable(Component.__table__, if_not_exists=True))
            await db.execute(CreateTable(Course.__table__, if_not_exists=True))
            await db.execute(CreateTable(Discussion.__table__, if_not_exists=True))
            await db.execute(CreateTable(DiscussionTopic.__table__, if_not_exists=True))
            await db.execute(CreateTable(DiscussionTopicReply.__table__, if_not_exists=True))
            await db.execute(CreateTable(File.__table__, if_not_exists=True))
            await db.execute(CreateTable(Notification.__table__, if_not_exists=True))
            await db.execute(CreateTable(Group.__table__, if_not_exists=True))
            await db.execute(CreateTable(SelectedCourse.__table__, if_not_exists=True))
            await db.execute(CreateTable(Subscription.__table__, if_not_exists=True))
            await db.execute(CreateTable(Bulletin.__table__, if_not_exists=True))
            await db.execute(CreateTable(Report.__table__, if_not_exists=True))
            await db.execute(CreateTable(ReportReply.__table__, if_not_exists=True))
            await db.execute(CreateTable(CourseMaterial.__table__, if_not_exists=True))
            await db.execute(CreateTable(MaterialInfo.__table__, if_not_exists=True))
            await db.execute(CreateTable(Assignment.__table__, if_not_exists=True))
            
            await FakeDB().create_entity_list(db)

            if not os.path.isdir("tmp"):
                os.mkdir("tmp")
            

async def close_db():
    async with SessionLocal() as db:
        async with db.begin():
            await db.execute(DropTable(Assignment.__table__))
            await db.execute(DropTable(MaterialInfo.__table__))
            await db.execute(DropTable(CourseMaterial.__table__))
            await db.execute(DropTable(ReportReply.__table__))
            await db.execute(DropTable(Report.__table__))
            await db.execute(DropTable(Bulletin.__table__))
            await db.execute(DropTable(Subscription.__table__))
            await db.execute(DropTable(SelectedCourse.__table__))
            await db.execute(DropTable(Group.__table__))
            await db.execute(DropTable(Notification.__table__))
            await db.execute(DropTable(File.__table__))
            await db.execute(DropTable(DiscussionTopicReply.__table__))
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
