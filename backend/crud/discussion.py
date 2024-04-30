from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel
from models.discussion import Discussion as DiscussionModel, DiscussionTopic as DiscussionTopicModel
from schemas import discussion as DiscussionSchema


@crud_class_decorator
class DiscussionCrudManager:
    async def create(self, uid: str, course_id: str, newDiscussion: DiscussionSchema.DiscussionCreate, db_session: AsyncSession):
        newDiscussion_dict = newDiscussion.model_dump()
        discussion = DiscussionModel(**newDiscussion_dict, uid=uid, course_id=course_id)
        db_session.add(discussion)
        await db_session.commit()

        return discussion

    async def get(self, discussion_id: int, db_session: AsyncSession):
        stmt = select(DiscussionModel).where(DiscussionModel.id == discussion_id)
        result = await db_session.execute(stmt)
        discussion = result.first()
        
        return discussion[0] if discussion else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [discussion[0] for discussion in result.all()]

    async def update(self, discussion_id: int, updateDiscussion: DiscussionSchema.DiscussionUpdate, db_session: AsyncSession):
        updateDiscussion_dict = updateDiscussion.model_dump(exclude_none=True)
        if updateDiscussion_dict:
            stmt = update(ComponentModel).where(ComponentModel.id == discussion_id).values(**updateDiscussion_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, discussion_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == discussion_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return


@crud_class_decorator
class DiscussionTopicCrudManager:
    async def create(self, uid: str, discussion_id: int, newTopic: DiscussionSchema.DiscussionCreate, db_session: AsyncSession):
        newTopic_dict = newTopic.model_dump()
        topic = DiscussionTopicModel(**newTopic_dict, uid=uid, discussion_id=discussion_id)
        db_session.add(topic)
        await db_session.commit()

        return topic

    async def get(self, topic_id: int, db_session: AsyncSession):
        stmt = select(DiscussionTopicModel).where(DiscussionTopicModel.id == topic_id)
        result = await db_session.execute(stmt)
        topic = result.first()
        
        return topic[0] if topic else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionTopicModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [topic[0] for topic in result.all()]

    async def update(self, topic_id: int, updateDiscussion: DiscussionSchema.DiscussionUpdate, db_session: AsyncSession):
        updateDiscussion_dict = updateDiscussion.model_dump(exclude_none=True)
        if updateDiscussion_dict:
            stmt = update(ComponentModel).where(ComponentModel.id == topic_id).values(**updateDiscussion_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, topic_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == topic_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
