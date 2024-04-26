from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.file import File as FileModel
from schemas import file as FileSchema


@crud_class_decorator
class FileCrudManager:
    async def create(self, component_id, path, db_session: AsyncSession):
        file = FileModel(component_id=component_id, path=path)
        db_session.add(file)
        await db_session.commit()

        return file
     
    async def get(self, file_id: str, db_session: AsyncSession):
        stmt = select(FileModel).where(FileModel.id == file_id)
        result = await db_session.execute(stmt)
        file = result.first()

        return file[0] if file else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(FileModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [file[0] for file in result.all()] 
    
    async def delete(self, file_id: int, db_session: AsyncSession):
        stmt = delete(FileModel).where(FileModel.id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    