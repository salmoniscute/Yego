from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.bulletin import CourseBulletin as CourseBulletinModel
from models.component import Component as ComponentModel
from schemas import course_bulletin as CourseBulletinSchema


@crud_class_decorator
class CourseBulletinCrudManager:
    async def create(self, uid: str, course_id: str, newBulletin: CourseBulletinSchema.CourseBulletinCreate, db_session: AsyncSession):
        newBulletin_dict = newBulletin.model_dump()
        bulletin = CourseBulletinModel(**newBulletin_dict, uid=uid, course_id=course_id)
        db_session.add(bulletin)
        await db_session.commit()
        db_session.refresh(bulletin)

        return bulletin

    async def get(self, bulletin_id: str, db_session: AsyncSession):
        stmt = select(CourseBulletinModel).where(CourseBulletinModel.id == bulletin_id)
        result = await db_session.execute(stmt)
        bulletin = result.first()
        
        return bulletin[0] if bulletin else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(CourseBulletinModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [bulletin[0] for bulletin in result.all()]

    async def update(self, bulletin_id: str, updateBulletin: CourseBulletinSchema.CourseBulletinUpdate, db_session: AsyncSession):
        updateBulletin_dict = updateBulletin.model_dump(exclude_none=True)
        if updateBulletin_dict:
            stmt = update(CourseBulletinModel).where(CourseBulletinModel.id == bulletin_id).values(**updateBulletin_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, bulletin_id: int, db_session: AsyncSession):
        stmt = delete(CourseBulletinModel).where(CourseBulletinModel.id == bulletin_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    