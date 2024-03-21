from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.discussion_topic_file import DiscussionTopicFile as DiscussionTopicFileModel
from schemas import discussion_topic_file as DiscussionTopicFileSchema

@crud_class_decorator
class DiscussionTopicFileCrudManager:
    async def create(self, topic_id, newDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileCreate, db_session: AsyncSession):
        newDiscussionTopicFile_dict = newDiscussionTopicFile.model_dump()
        discussion_topic_file = DiscussionTopicFileModel(**newDiscussionTopicFile_dict, topic_id=topic_id)
        db_session.add(discussion_topic_file)
        await db_session.commit()
        db_session.refresh(discussion_topic_file)

        return discussion_topic_file

    async def get(self, file_id: str, db_session: AsyncSession):
        stmt = select(DiscussionTopicFileModel).where(DiscussionTopicFileModel.file_id == file_id)
        result = await db_session.execute(stmt)
        discussion_topic_file = result.first()
        
        return discussion_topic_file[0] if discussion_topic_file else None
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionTopicFileModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [discussion_topic_file[0] for discussion_topic_file in result.all()]

    async def update(self, file_id: str, updateDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileUpdate, db_session: AsyncSession):
        updateDiscussionTopicFile_dict = updateDiscussionTopicFile.model_dump()
        if updateDiscussionTopicFile_dict:
            stmt = update(DiscussionTopicFileModel).where(DiscussionTopicFileModel.file_id == file_id).values(**updateDiscussionTopicFile_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    
    async def delete(self, file_id: int, db_session: AsyncSession):
        stmt = delete(DiscussionTopicFileModel).where(DiscussionTopicFileModel.file_id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    