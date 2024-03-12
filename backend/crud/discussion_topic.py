from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.discussion_topic import Discussion_topic as DiscussionTopicModel
from schemas import discussion_topic as DiscussionTopicSchema

@crud_class_decorator
class DiscussionTopicCrudManager:
    async def create_discussion_topic(self, newDiscussion: DiscussionTopicSchema.DiscussionTopicCreate, db_session: AsyncSession):
        discussion_topic = DiscussionTopicModel(
            topic_id=newDiscussion.topic_id,
            discussion_id=newDiscussion.discussion_id,
            publisher=newDiscussion.publisher,
            title=newDiscussion.title,
            release_time=newDiscussion.release_time,
            content=newDiscussion.content
        )
        db_session.add(discussion_topic)
        await db_session.commit()
        db_session.refresh(discussion_topic)

        return discussion_topic

    async def get_discussion_topic_by_topic_id(self, topic_id: str, db_session: AsyncSession):
        stmt = select(
            DiscussionTopicModel.topic_id,
            DiscussionTopicModel.discussion_id,
            DiscussionTopicModel.publisher,
            DiscussionTopicModel.title,
            DiscussionTopicModel.release_time,
            DiscussionTopicModel.content
        ).where(DiscussionTopicModel.topic_id == topic_id)
        result = await db_session.execute(stmt)
        discussion_topic = result.first()
        if discussion_topic:
            return discussion_topic
        
        return None

    async def update_discussion_topic_by_topic_id(self, topic_id: str, updatediscussion: DiscussionTopicSchema.DiscussionTopicUpdate, db_session: AsyncSession):
        stmt = update(DiscussionTopicModel).where(DiscussionTopicModel.topic_id == topic_id).values(
            publisher=updatediscussion.publisher,
            title=updatediscussion.title,
            release_time=updatediscussion.release_time,
            content=updatediscussion.content
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_discussion_topic_by_topic_id(self, topic_id: int, db_session: AsyncSession):
        stmt = delete(DiscussionTopicModel).where(DiscussionTopicModel.topic_id == topic_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    