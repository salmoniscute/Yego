from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.course_bulletin import Course_bulletin as CourseBulletinModel
from schemas import course_bulletin as CourseBulletinSchema

@crud_class_decorator
class CourseBulletinCrudManager:
    async def create_course_bulletin(self, newCourse: CourseBulletinSchema.CourseBulletinCreate, db_session: AsyncSession):
        course_bulletin = CourseBulletinModel(
            cb_id = newCourse.cb_id,
            publisher = newCourse.publisher,
            course_id = newCourse.course_id,
            title = newCourse.title,
            release_time = newCourse.release_time,
            content = newCourse.content
        )
        db_session.add(course_bulletin)
        await db_session.commit()
        db_session.refresh(course_bulletin)

        return course_bulletin

    async def get_course_bulletin_by_cb_id(self, cb_id: str, db_session: AsyncSession):
        stmt = select(
            CourseBulletinModel.cb_id,
            CourseBulletinModel.publisher,
            CourseBulletinModel.course_id,
            CourseBulletinModel.title,
            CourseBulletinModel.release_time,
            CourseBulletinModel.content
        ).where(CourseBulletinModel.cb_id == cb_id)
        result = await db_session.execute(stmt)
        course_bulletin = result.first()
        if course_bulletin:
            return course_bulletin
        return None

    async def update_course_bulletin_by_id(self, course_id: str, updateCourseBulletin: CourseBulletinSchema.CourseBulletinUpdate, db_session: AsyncSession):
        stmt = update(CourseBulletinModel).where(CourseBulletinModel.course_id == course_id).values(
            publisher=updateCourseBulletin.publisher,
            title=updateCourseBulletin.title,
            release_time=updateCourseBulletin.release_time,
            content=updateCourseBulletin.content
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    
    async def delete_course_bulletin_by_id(self, course_id: int, db_session: AsyncSession):
        stmt = delete(CourseBulletinModel).where(CourseBulletinModel.course_id == course_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    