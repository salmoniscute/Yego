from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.file import File as FileModel
from schemas import file as FileSchema


@crud_class_decorator
class FileCrudManager:
    async def create(self, component_id, newFile: FileSchema.FileCreate, db_session: AsyncSession):
        newFile_dict = newFile.model_dump()
        file = FileModel(component_id=component_id, **newFile_dict)
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
    
    async def update(self, file_id: str, updateFile: FileSchema.FileUpdate, db_session: AsyncSession):
        updateFile_dict = updateFile.model_dump(exclude_none=True)
        if updateFile_dict:
            stmt = update(FileModel).where(FileModel.id == file_id).values(updateFile_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, file_id: int, db_session: AsyncSession):
        stmt = delete(FileModel).where(FileModel.id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    