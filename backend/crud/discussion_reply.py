from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.discussion_reply import Discussion_reply as DiscussionReplyModel
from schemas import discussion_reply as DiscussionReplySchema

@crud_class_decorator
class DiscussionReplyCrudManager:
    async def create_discussion_reply(self, newDiscussionReply: DiscussionReplySchema.DiscussionReplyCreate, db_session: AsyncSession):
        discussion_reply = DiscussionReplyModel(
            reply_id=newDiscussionReply.reply_id,
            topic_id=newDiscussionReply.topic_id,
            publisher=newDiscussionReply.publisher,
            release_time=newDiscussionReply.release_time,
            content=newDiscussionReply.content
        )
        db_session.add(discussion_reply)
        await db_session.commit()
        db_session.refresh(discussion_reply)

        return discussion_reply

    async def get_discussion_reply_by_reply_id(self, reply_id: str, db_session: AsyncSession):
        stmt = select(
            DiscussionReplyModel.reply_id,
            DiscussionReplyModel.topic_id,
            DiscussionReplyModel.publisher,
            DiscussionReplyModel.release_time,
            DiscussionReplyModel.content
        ).where(DiscussionReplyModel.reply_id == reply_id)
        result = await db_session.execute(stmt)
        discussion_reply = result.first()
        if discussion_reply:
            return discussion_reply
        
        return None

    async def update_discussion_reply_by_reply_id(self, reply_id: str, updateDiscussionReply: DiscussionReplySchema.DiscussionReplyUpdate, db_session: AsyncSession):
        stmt = update(DiscussionReplyModel).where(DiscussionReplyModel.reply_id == reply_id).values(
            publisher=updateDiscussionReply.publisher,
            release_time=updateDiscussionReply.release_time,
            content=updateDiscussionReply.content   
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_discussion_reply_by_reply_id(self, reply_id: int, db_session: AsyncSession):
        stmt = delete(DiscussionReplyModel).where(DiscussionReplyModel.reply_id == reply_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    