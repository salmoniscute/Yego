from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.website_bulletin_file import WebsiteBulletinFile as WebsiteBulletinFileModel
from schemas import website_bulletin_file as WebsiteBulletinFileSchema


@crud_class_decorator
class WebsiteBulletinFileCrudManager:
    async def create_file(self, newFile: WebsiteBulletinFileSchema.WebsiteBulletinFileCreate, db_session: AsyncSession):
        file = WebsiteBulletinFileModel(
            file_id=newFile.file_id,
            wb_id=newFile.wb_id,
            path=newFile.path
        )
        db_session.add(file)
        await db_session.commit()
        db_session.refresh(file)

        return file

    async def get_file_by_file_id(self, file_id: str, db_session: AsyncSession):
        stmt = select(
            WebsiteBulletinFileModel.file_id,
            WebsiteBulletinFileModel.wb_id,
            WebsiteBulletinFileModel.path
        ).where(WebsiteBulletinFileModel.file_id == file_id)
        result = await db_session.execute(stmt)
        file = result.first()

        if file:
            return file
        
        return None

    async def update_file_by_file_id(self, file_id: str, newFile: WebsiteBulletinFileSchema.WebsiteBulletinFileUpdate, db_session: AsyncSession):
        stmt = update(WebsiteBulletinFileModel).where(WebsiteBulletinFileModel.file_id == file_id).values(
            path=newFile.path
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    
    async def delete_file_by_file_id(self, file_id: int, db_session: AsyncSession):
        stmt = delete(WebsiteBulletinFileModel).where(WebsiteBulletinFileModel.file_id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    