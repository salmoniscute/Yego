from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.course_bulletin import CourseBulletin as CourseBulletinModel
from schemas import course_bulletin as CourseBulletinSchema

@crud_class_decorator
class CourseBulletinCrudManager:
    async def create(self, course_id, newCourseBulletin: CourseBulletinSchema.CourseBulletinCreate, db_session: AsyncSession):
        newCourseBulletin_dict = newCourseBulletin.model_dump()
        course_bulletin = CourseBulletinModel(**newCourseBulletin_dict, course_id=course_id)
        db_session.add(course_bulletin)
        await db_session.commit()
        db_session.refresh(course_bulletin)

        return course_bulletin

    async def get(self, cb_id: str, db_session: AsyncSession):
        stmt = select(CourseBulletinModel).where(CourseBulletinModel.cb_id == cb_id)
        result = await db_session.execute(stmt)
        course_bulletin = result.first()
        
        return course_bulletin[0] if course_bulletin else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(CourseBulletinModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [course_bulletin[0] for course_bulletin in result.all()]

    async def update(self, cb_id: str, updateCourseBulletin: CourseBulletinSchema.CourseBulletinUpdate, db_session: AsyncSession):
        updateCourseBulletin_dict = updateCourseBulletin.model_dump()
        if updateCourseBulletin_dict:
            stmt = update(CourseBulletinModel).where(CourseBulletinModel.cb_id == cb_id).values(**updateCourseBulletin_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    
    async def delete(self, cb_id: int, db_session: AsyncSession):
        stmt = delete(CourseBulletinModel).where(CourseBulletinModel.cb_id == cb_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    