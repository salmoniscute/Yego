from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.component import Component as ComponentModel
from models.discussion import Discussion as DiscussionModel
from schemas import discussion as DiscussionSchema


@crud_class_decorator
class DiscussionCrudManager:
    async def create(self, uid: str, course_id: str, newDiscussion: DiscussionSchema.DiscussionCreate, db_session: AsyncSession):
        newDiscussion_dict = newDiscussion.model_dump()
        discussion = DiscussionModel(**newDiscussion_dict, uid=uid, course_id=course_id)
        db_session.add(discussion)
        await db_session.commit()

        return discussion

    async def get(self, discussion_id: str, db_session: AsyncSession):
        stmt = select(DiscussionModel).where(DiscussionModel.id == discussion_id)
        result = await db_session.execute(stmt)
        discussion = result.first()
        
        return discussion[0] if discussion else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [discussion[0] for discussion in result.all()]

    async def update(self, discussion_id: str, updateDiscussion: DiscussionSchema.DiscussionRead, db_session: AsyncSession):
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
