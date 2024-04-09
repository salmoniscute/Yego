from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.bulletin import CourseBulletin as CourseBulletinModel, WebsiteBulletin as WebsiteBulletinModel
from models.component import Component as ComponentModel
from schemas import bulletin as BulletinSchema


@crud_class_decorator
class CourseBulletinCrudManager:
    async def create(self, uid: str, course_id: str, newBulletin: BulletinSchema.BulletinCreate, db_session: AsyncSession):
        newBulletin_dict = newBulletin.model_dump()
        bulletin = CourseBulletinModel(**newBulletin_dict, uid=uid, course_id=course_id)
        db_session.add(bulletin)
        await db_session.commit()

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

    async def update(self, bulletin_id: str, updateBulletin: BulletinSchema.BulletinUpdate, db_session: AsyncSession):
        update_bulletin = {}
        update_component = updateBulletin.model_dump(exclude_none=True)
        tmp = update_component.pop("pin_to_top", None)
        if tmp is not None:
            update_bulletin["pin_to_top"] = tmp

        if update_component:
            stmt = update(ComponentModel).where(ComponentModel.id == bulletin_id).values(**update_component)
            await db_session.execute(stmt)
            await db_session.commit()

        if update_bulletin:
            stmt = update(CourseBulletinModel).where(CourseBulletinModel.id == bulletin_id).values(**update_bulletin)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, bulletin_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == bulletin_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    

@crud_class_decorator
class WebsiteBulletinCrudManager:
    async def create(self, uid: str, newBulletin: BulletinSchema.BulletinCreate, db_session: AsyncSession):
        newBulletin_dict = newBulletin.model_dump()
        bulletin = WebsiteBulletinModel(**newBulletin_dict, uid=uid)
        db_session.add(bulletin)
        await db_session.commit()

        return bulletin

    async def get(self, bulletin_id: str, db_session: AsyncSession):
        stmt = select(WebsiteBulletinModel).where(WebsiteBulletinModel.id == bulletin_id)
        result = await db_session.execute(stmt)
        bulletin = result.first()
        
        return bulletin[0] if bulletin else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(WebsiteBulletinModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [bulletin[0] for bulletin in result.all()]

    async def update(self, bulletin_id: str, updateBulletin: BulletinSchema.BulletinUpdate, db_session: AsyncSession):
        update_bulletin = {}
        update_component = updateBulletin.model_dump(exclude_none=True)
        tmp = update_component.pop("pin_to_top", None)
        if tmp is not None:
            update_bulletin["pin_to_top"] = tmp

        if update_component:
            stmt = update(ComponentModel).where(ComponentModel.id == bulletin_id).values(**update_component)
            await db_session.execute(stmt)
            await db_session.commit()

        if update_bulletin:
            stmt = update(WebsiteBulletinModel).where(WebsiteBulletinModel.id == bulletin_id).values(**update_bulletin)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, bulletin_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == bulletin_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    