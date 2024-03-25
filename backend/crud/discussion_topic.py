from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.discussion_topic import DiscussionTopic as DiscussionTopicModel
from schemas import discussion_topic as DiscussionTopicSchema

@crud_class_decorator
class DiscussionTopicCrudManager:
    async def create(self, discussion_id, publisher, newDiscussionTopic: DiscussionTopicSchema.DiscussionTopicCreate, db_session: AsyncSession):
        newDiscussionTopic_dict = newDiscussionTopic.model_dump()
        discussion_topic = DiscussionTopicModel(**newDiscussionTopic_dict, discussion_id=discussion_id, publisher=publisher)
        db_session.add(discussion_topic)
        await db_session.commit()
        db_session.refresh(discussion_topic)

        return discussion_topic

    async def get(self, topic_id: str, db_session: AsyncSession):
        stmt = select(DiscussionTopicModel).where(DiscussionTopicModel.topic_id == topic_id)
        result = await db_session.execute(stmt)
        discussion_topic = result.first()
        
        return discussion_topic[0] if discussion_topic else None
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionTopicModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [discussion_topic[0] for discussion_topic in result.all()]

    async def update(self, topic_id: str, updateDiscussionTopic: DiscussionTopicSchema.DiscussionTopicUpdate, db_session: AsyncSession):
        updateDiscussionTopic_dict = updateDiscussionTopic.model_dump()
        if updateDiscussionTopic_dict:
            stmt = update(DiscussionTopicModel).where(DiscussionTopicModel.topic_id == topic_id).values(**updateDiscussionTopic_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    
    async def delete(self, topic_id: int, db_session: AsyncSession):
        stmt = delete(DiscussionTopicModel).where(DiscussionTopicModel.topic_id == topic_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    