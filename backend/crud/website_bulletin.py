from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.website_bulletin import WebsiteBulletin as WebsiteBulletinModel
from schemas import website_bulletin as WebsiteBulletinSchema


@crud_class_decorator
class WebsiteBulletinCrudManager:
    async def create_website_bulletin(self, newBulletin: WebsiteBulletinSchema.WebsiteBulletinCreate, db_session: AsyncSession):
        website_bulletin = WebsiteBulletinModel(
            wb_id = newBulletin.wb_id,
            publisher = newBulletin.publisher,
            title = newBulletin.title,
            release_time = newBulletin.release_time,
            content = newBulletin.content,
            pin_to_top=newBulletin.pin_to_top
        )
        db_session.add(website_bulletin)
        await db_session.commit()
        db_session.refresh(website_bulletin)

        return website_bulletin

    async def get_website_bulletin_by_wb_id(self, wb_id: str, db_session: AsyncSession):
        stmt = select(
            WebsiteBulletinModel.wb_id,
            WebsiteBulletinModel.publisher,
            WebsiteBulletinModel.title,
            WebsiteBulletinModel.release_time,
            WebsiteBulletinModel.content,
            WebsiteBulletinModel.pin_to_top
        ).where(WebsiteBulletinModel.wb_id == wb_id)
        result = await db_session.execute(stmt)
        website_bulletin = result.first()

        if website_bulletin:
            return website_bulletin
        
        return None

    async def update_website_bulletin_by_wb_id(self, wb_id: str, newBulletin: WebsiteBulletinSchema.WebsiteBulletinUpdate, db_session: AsyncSession):
        stmt = update(WebsiteBulletinModel).where(WebsiteBulletinModel.wb_id == wb_id).values(
            title=newBulletin.title,
            content=newBulletin.content,
            pin_to_top=newBulletin.pin_to_top
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    
    async def delete_website_bulletin_by_wb_id(self, wb_id: int, db_session: AsyncSession):
        stmt = delete(WebsiteBulletinModel).where(WebsiteBulletinModel.wb_id == wb_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    