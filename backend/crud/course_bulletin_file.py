from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.course_bulletin_file import CourseBulletinFile as CourseBulletinFileModel
from schemas import course_bulletin_file as CourseBulletinFileSchema

@crud_class_decorator
class CourseBulletinFileCrudManager:
    async def create(self, cb_id, newCourseBulletinFile: CourseBulletinFileSchema.CourseBulletinFileCreate, db_session: AsyncSession):
        newCourseBulletinFile_dict = newCourseBulletinFile.model_dump()
        course_bulletin_file = CourseBulletinFileModel(**newCourseBulletinFile_dict, cb_id=cb_id)
        db_session.add(course_bulletin_file)
        await db_session.commit()
        db_session.refresh(course_bulletin_file)

        return course_bulletin_file

    async def get(self, file_id: str, db_session: AsyncSession):
        stmt = select(CourseBulletinFileModel).where(CourseBulletinFileModel.file_id == file_id)
        result = await db_session.execute(stmt)
        course_bulletin_file = result.first()
        
        return course_bulletin_file[0] if course_bulletin_file else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(CourseBulletinFileModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [course_bulletin_file[0] for course_bulletin_file in result.all()]

    async def update(self, file_id: str, updateCourseBulletin: CourseBulletinFileSchema.CourseBulletinFileUpdate, db_session: AsyncSession):
        updateCourseBulletin_dict = updateCourseBulletin.model_dump()
        if updateCourseBulletin_dict:
            stmt = update(CourseBulletinFileModel).where(CourseBulletinFileModel.file_id == file_id).values(**updateCourseBulletin_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    
    async def delete(self, file_id: int, db_session: AsyncSession):
        stmt = delete(CourseBulletinFileModel).where(CourseBulletinFileModel.file_id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    