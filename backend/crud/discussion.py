from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from crud.component import ComponentCrudManager
from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel
from models.discussion import Discussion as DiscussionModel, DiscussionTopic as DiscussionTopicModel, DiscussionTopicReply as DiscussionTopicReplyModel
from schemas import discussion as DiscussionSchema

ComponentCrud = ComponentCrudManager()

@crud_class_decorator
class DiscussionCrudManager:
    async def create(self, uid: str, course_id: str, newDiscussion: DiscussionSchema.DiscussionCreate, db_session: AsyncSession):
        newComponent_dict = newDiscussion.model_dump()
        component = await ComponentCrud.create(uid, newComponent_dict)
        
        discussion = DiscussionModel(id=component.id, course_id=course_id)
        db_session.add(discussion)
        await db_session.commit()
        
        return discussion


    async def get(self, discussion_id: int, db_session: AsyncSession):
        stmt = select(DiscussionModel).where(DiscussionModel.id == discussion_id)
        result = await db_session.execute(stmt)
        discussion = result.first()
        obj = {}
        if discussion:
            await db_session.refresh(discussion[0], ["info"])
            obj = {
                "id": discussion[0].id,
                "uid": discussion[0].info.uid,
                "release_time": discussion[0].info.release_time,
                "title": discussion[0].info.title,
                "content": discussion[0].info.content,
                "publisher": discussion[0].info.publisher_info.name,
                "avatar": discussion[0].info.publisher_info.avatar,
                "files": [file for file in discussion[0].info.files],
                "subscription": True if discussion[0].info.subscriptions else False
            }
        return obj

    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionModel)
        result = await db_session.execute(stmt)
        obj = {}
        _list = []
        for discussion in result.all():
            await db_session.refresh(discussion[0], ["info"])
            obj = {
                "id": discussion[0].id,
                "uid": discussion[0].info.uid,
                "release_time": discussion[0].info.release_time,
                "title": discussion[0].info.title,
                "content": discussion[0].info.content,
                "publisher": discussion[0].info.publisher_info.name,
                "avatar": discussion[0].info.publisher_info.avatar,
                "files": [file for file in discussion[0].info.files],
                "subscription": True if discussion[0].info.subscriptions else False
            }
            _list.append(obj)
        
        return _list
    
    async def update(self, discussion_id: int, updateDiscussion: DiscussionSchema.DiscussionUpdate, db_session: AsyncSession):
        updateDiscussion_dict = updateDiscussion.model_dump(exclude_none=True)
        if updateDiscussion_dict:
            await ComponentCrud.update(discussion_id, updateDiscussion_dict)

        return
    
    async def delete(self, discussion_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == discussion_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def get_discussions_by_course_id(self, course_id: str, db_session: AsyncSession):
        stmt = select(DiscussionModel).where(DiscussionModel.course_id == course_id)
        result = await db_session.execute(stmt)
        result = result.unique()
        output = []
        for discussion in result.all():
            await db_session.refresh(discussion[0], ["info"])
            d = {
                "id": discussion[0].id,
                "uid": discussion[0].info.uid,
                "title": discussion[0].info.title,
                "content": discussion[0].info.content,
                "subscription": True if discussion[0].info.subscriptions else False
            }
            output.append(d)
        return output


@crud_class_decorator
class DiscussionTopicCrudManager:
    async def create(self, uid: str, discussion_id: int, newTopic: DiscussionSchema.DiscussionCreate, db_session: AsyncSession):
        newComponent_dict = newTopic.model_dump()
        component = await ComponentCrud.create(uid, newComponent_dict)
        
        topic = DiscussionTopicModel(id=component.id, discussion_id=discussion_id)
        db_session.add(topic)
        await db_session.commit()
        
        return topic

    async def get(self, topic_id: int, db_session: AsyncSession):
        stmt = select(DiscussionTopicModel).where(DiscussionTopicModel.id == topic_id)
        result = await db_session.execute(stmt)
        topic = result.first()
        obj = {}
        if topic:
            await db_session.refresh(topic[0], ["info"])
            obj = {
                "id": topic[0].id,
                "uid": topic[0].info.uid,
                "title": topic[0].info.title,
                "content": topic[0].info.content,
                "discussion_id": topic[0].discussion_id
            }        
        return obj

    async def get_all(self, db_session: AsyncSession):
        stmt = select(DiscussionTopicModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        obj = {}
        _list = []
        for topic in result.all():
            await db_session.refresh(topic[0], ["info"])
            obj = {
                "id": topic[0].id,
                "uid": topic[0].info.uid,
                "title": topic[0].info.title,
                "content": topic[0].info.content,
                "discussion_id": topic[0].discussion_id
            }
            _list.append(obj)
        
        return _list
    
    async def get_topics_by_discussion_id(self, discussion_id: int, db_session: AsyncSession):
        stmt = select(DiscussionTopicModel).where(DiscussionTopicModel.discussion_id == discussion_id)
        result = await db_session.execute(stmt)
        result = result.unique()
        _list = []
        for topic in result.all():
            await db_session.refresh(topic[0], ["info"])
            stmt = select(DiscussionTopicReplyModel).where(DiscussionTopicReplyModel.root_id == topic[0].id) 
            record = await db_session.execute(stmt)
            replies = len(record.all())
            t = {
                "id": topic[0].id,
                "uid": topic[0].info.uid,
                "release_time": topic[0].info.release_time,
                "title": topic[0].info.title,
                "content": topic[0].info.content,
                "reply_count": replies,
                "publisher": topic[0].info.publisher_info.name,
                "avatar": topic[0].info.publisher_info.avatar,
                "files": [file for file in topic[0].info.files],
                "subscription": True if topic[0].info.subscriptions else False
            }
            _list.append(t)
        return _list
            

    async def update(self, topic_id: int, updateDiscussion: DiscussionSchema.DiscussionUpdate, db_session: AsyncSession):
        updateDiscussion_dict = updateDiscussion.model_dump(exclude_none=True)
        if updateDiscussion_dict:
            await ComponentCrud.update(topic_id, updateDiscussion_dict)

        return
    
    async def delete(self, topic_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == topic_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return

@crud_class_decorator
class DiscussionTopicReplyCrudManager:
    async def create(self, uid: str, root_id: int, parent_id: int, newReply: DiscussionSchema.DiscussionTopicReplyCreate, db_session: AsyncSession):
        newComponent_dict = newReply.model_dump()
        newComponent_dict["title"] = "None"
        component = await ComponentCrud.create(uid=uid, newComponent=newComponent_dict)
        
        reply = DiscussionTopicReplyModel(id=component.id, root_id=root_id, parent_id=parent_id)
        db_session.add(reply)
        await db_session.commit()
        
        return reply

    async def get(self, reply_id: int, db_session: AsyncSession):
        stmt = select(DiscussionTopicReplyModel).where(DiscussionTopicReplyModel.id == reply_id)
        result = await db_session.execute(stmt)
        reply = result.first()
        obj = {}
        if reply:
            await db_session.refresh(reply[0], ["info"])
            obj = {
                "id": reply[0].id,
                "uid": reply[0].info.uid,
                "parent_id": reply[0].parent_id,
                "root_id": reply[0].root_id,
                "title": reply[0].info.title,
                "content": reply[0].info.content,
            }
        return obj

    async def update(self, reply_id: int, updateDiscussion: DiscussionSchema.DiscussionUpdate, db_session: AsyncSession):
        updateDiscussion_dict = updateDiscussion.model_dump(exclude_none=True)
        if updateDiscussion_dict:
            await ComponentCrud.update(reply_id, updateDiscussion_dict)

        return
    
    async def delete(self, reply_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == reply_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return