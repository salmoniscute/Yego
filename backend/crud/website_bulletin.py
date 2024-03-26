from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.website_bulletin import WebsiteBulletin as WebsiteBulletinModel
from schemas import website_bulletin as WebsiteBulletinSchema


@crud_class_decorator
class WebsiteBulletinCrudManager:
    async def get(self, wb_id: str, db_session: AsyncSession):
        stmt = select(WebsiteBulletinModel).where(WebsiteBulletinModel.wb_id == wb_id)
        result = await db_session.execute(stmt)
        bulletin = result.first()

        return bulletin[0] if bulletin else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(WebsiteBulletinModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [bulletin[0] for bulletin in result.all()]
    
    async def create(self, publisher: str, newBulletin: WebsiteBulletinSchema.WebsiteBulletinCreate, db_session: AsyncSession):
        newBulletin_dict = newBulletin.model_dump()
        bulletin = WebsiteBulletinModel(publisher=publisher, **newBulletin_dict)
        db_session.add(bulletin)
        await db_session.commit()
        db_session.refresh(bulletin)

        return bulletin
    
    async def update(self, wb_id: str, newBulletin: WebsiteBulletinSchema.WebsiteBulletinUpdate, db_session: AsyncSession):
        updateBulletin_dict = newBulletin.model_dump(exclude_none=True)
        if updateBulletin_dict:
            stmt = update(WebsiteBulletinModel).where(WebsiteBulletinModel.wb_id == wb_id).values(updateBulletin_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, wb_id: int, db_session: AsyncSession):
        stmt = delete(WebsiteBulletinModel).where(WebsiteBulletinModel.wb_id == wb_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    