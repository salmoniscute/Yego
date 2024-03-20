from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.discussion_topic_file import DiscussionTopicFile as DiscussionTopicFileModel
from schemas import discussion_topic_file as DiscussionTopicFileSchema

@crud_class_decorator
class DiscussionTopicFileCrudManager:
    async def create_discussion_topic_file(self, newDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileCreate, db_session: AsyncSession):
        discussion_topic_file = DiscussionTopicFileModel(
            file_id=newDiscussionTopicFile.file_id,
            topic_id=newDiscussionTopicFile.topic_id,
            path=newDiscussionTopicFile.path
        )
        db_session.add(discussion_topic_file)
        await db_session.commit()
        db_session.refresh(discussion_topic_file)

        return discussion_topic_file

    async def get_discussion_topic_file_by_file_id(self, file_id: str, db_session: AsyncSession):
        stmt = select(
            DiscussionTopicFileModel.file_id,
            DiscussionTopicFileModel.topic_id,
            DiscussionTopicFileModel.path
        ).where(DiscussionTopicFileModel.file_id == file_id)
        result = await db_session.execute(stmt)
        discussion_topic_file = result.first()
        if discussion_topic_file:
            return discussion_topic_file
        
        return None

    async def update_discussion_topic_file_by_file_id(self, file_id: str, updateDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileUpdate, db_session: AsyncSession):
        stmt = update(DiscussionTopicFileModel).where(DiscussionTopicFileModel.file_id == file_id).values(
            path=updateDiscussionTopicFile.path
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_discussion_topic_file_by_file_id(self, file_id: int, db_session: AsyncSession):
        stmt = delete(DiscussionTopicFileModel).where(DiscussionTopicFileModel.file_id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    