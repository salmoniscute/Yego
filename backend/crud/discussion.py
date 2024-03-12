from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.discussion import Discussion as DiscussionModel
from schemas import discussion as DiscussionSchema

@crud_class_decorator
class DiscussionCrudManager:
    async def create_discussion(self, newDiscussion: DiscussionSchema.DiscussionCreate, db_session: AsyncSession):
        discussion = DiscussionModel(
            discussion_id=newDiscussion.discussion_id,
            course_id=newDiscussion.course_id,
            title=newDiscussion.title,
            discription=newDiscussion.discription
        )
        db_session.add(discussion)
        await db_session.commit()
        db_session.refresh(discussion)

        return discussion

    async def get_discussion_by_id(self, discussion_id: str, db_session: AsyncSession):
        stmt = select(
            DiscussionModel.discussion_id,
            DiscussionModel.course_id,
            DiscussionModel.title,
            DiscussionModel.discription
        ).where(DiscussionModel.discussion_id == discussion_id)
        result = await db_session.execute(stmt)
        discussion = result.first()
        if discussion:
            return discussion
        
        return None

    async def update_discussion_by_id(self, discussion_id: str, updatediscussion: DiscussionSchema.DiscussionUpdate, db_session: AsyncSession):
        stmt = update(DiscussionModel).where(DiscussionModel.discussion_id == discussion_id).values(
            title=updatediscussion.title,
            discription=updatediscussion.discription
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_discussion_by_id(self, discussion_id: int, db_session: AsyncSession):
        stmt = delete(DiscussionModel).where(DiscussionModel.discussion_id == discussion_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    