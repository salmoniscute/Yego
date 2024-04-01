from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.discussion_reply import DiscussionReply as DiscussionReplyModel
from schemas import discussion_reply as DiscussionReplySchema

@crud_class_decorator
class DiscussionReplyCrudManager:
    async def create(self, parent, topic_id, publisher, newDiscussionReply: DiscussionReplySchema.DiscussionReplyCreate, db_session: AsyncSession):
        newDiscussionReply_dict = newDiscussionReply.model_dump()
        discussion_reply = DiscussionReplyModel(**newDiscussionReply_dict, parent=parent, topic_id=topic_id, publisher=publisher)
        db_session.add(discussion_reply)
        await db_session.commit()
        db_session.refresh(discussion_reply)

        return discussion_reply

    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionReplyModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [discussion_reply[0] for discussion_reply in result.all()]

    async def get(self, reply_id: str, db_session: AsyncSession):
        stmt = select(DiscussionReplyModel).where(DiscussionReplyModel.reply_id == reply_id)
        result = await db_session.execute(stmt)
        discussion_reply = result.first()
        
        return discussion_reply[0] if discussion_reply else None

    async def update(self, reply_id: str, updateDiscussionReply: DiscussionReplySchema.DiscussionReplyUpdate, db_session: AsyncSession):
        updateDiscussionReply_dict = updateDiscussionReply.model_dump()
        if updateDiscussionReply_dict:
            stmt = update(DiscussionReplyModel).where(DiscussionReplyModel.reply_id == reply_id).values(**updateDiscussionReply_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    
    async def delete(self, reply_id: int, db_session: AsyncSession):
        stmt = delete(DiscussionReplyModel).where(DiscussionReplyModel.reply_id == reply_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    