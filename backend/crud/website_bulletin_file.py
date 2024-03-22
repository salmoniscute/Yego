from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.website_bulletin_file import WebsiteBulletinFile as WebsiteBulletinFileModel
from schemas import website_bulletin_file as WebsiteBulletinFileSchema


@crud_class_decorator
class WebsiteBulletinFileCrudManager:
    async def get(self, file_id: str, db_session: AsyncSession):
        stmt = select(WebsiteBulletinFileModel).where(WebsiteBulletinFileModel.file_id == file_id)
        result = await db_session.execute(stmt)
        file = result.first()

        return file[0] if file else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(WebsiteBulletinFileModel)
        result = await db_session.execute(stmt)

        return [file[0] for file in result.all()]
    
    async def create(self, wb_id, newFile: WebsiteBulletinFileSchema.WebsiteBulletinFileCreate, db_session: AsyncSession):
        newFile_dict = newFile.model_dump()
        file = WebsiteBulletinFileModel(wb_id=wb_id, **newFile_dict)
        db_session.add(file)
        await db_session.commit()
        db_session.refresh(file)

        return file
    
    async def update(self, file_id: str, updateFile: WebsiteBulletinFileSchema.WebsiteBulletinFileUpdate, db_session: AsyncSession):
        updateFile_dict = updateFile.model_dump(exclude_none=True)
        if updateFile_dict:
            stmt = update(WebsiteBulletinFileModel).where(WebsiteBulletinFileModel.file_id == file_id).values(updateFile_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, file_id: int, db_session: AsyncSession):
        stmt = delete(WebsiteBulletinFileModel).where(WebsiteBulletinFileModel.file_id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    