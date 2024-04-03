from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.bulletin import Bulletin as BulletinModel
from models.component import Component as ComponentModel
from schemas import bulletin as BulletinSchema

@crud_class_decorator
class BulletinCrudManager:
    async def create(self, uid: str, course_id: str, newBulletin: BulletinSchema.BulletinCreate, db_session: AsyncSession):
        newBulletin_dict = newBulletin.model_dump()
        bulletin = BulletinModel(**newBulletin_dict, course_id=course_id, uid=uid)
        db_session.add(bulletin)
        await db_session.commit()
        db_session.refresh(bulletin)

        return bulletin

    async def get(self, bulletin_id: str, db_session: AsyncSession):
        stmt = select(BulletinModel).where(BulletinModel.id == bulletin_id)
        result = await db_session.execute(stmt)
        bulletin = result.first()
        
        return bulletin[0] if bulletin else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(BulletinModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [bulletin[0] for bulletin in result.all()]

    async def update(self, bulletin_id: str, updateBulletin: BulletinSchema.BulletinUpdate, db_session: AsyncSession):
        updateBulletin_dict = updateBulletin.model_dump(exclude_none=True)
        if updateBulletin_dict:
            stmt = update(BulletinModel).where(BulletinModel.id == bulletin_id).values(**updateBulletin_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, bulletin_id: int, db_session: AsyncSession):
        stmt = delete(BulletinModel).where(BulletinModel.id == bulletin_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    