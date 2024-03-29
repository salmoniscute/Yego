from fastapi import HTTPException

from crud.user import UserCrudManager
from crud.course import CourseCrudManager
from crud.selected_course import SelectedCourseCrudManager
from crud.website_bulletin import WebsiteBulletinCrudManager
from crud.website_bulletin_file import WebsiteBulletinFileCrudManager
from crud.course_bulletin import CourseBulletinCrudManager
from crud.discussion import DiscussionCrudManager
from crud.discussion_topic import DiscussionTopicCrudManager
from crud.discussion_reply import DiscussionReplyCrudManager
from crud.discussion_topic_file import DiscussionTopicFileCrudManager
from crud.course_bulletin_file import CourseBulletinFileCrudManager

UserCrud = UserCrudManager()
CourseCrud = CourseCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
WebsiteBulletinCrud = WebsiteBulletinCrudManager()
WebsiteBulletinFileCrud = WebsiteBulletinFileCrudManager()
CourseBulletinCrud = CourseBulletinCrudManager()
DiscussionCrud = DiscussionCrudManager()
DiscussionTopicCrud = DiscussionTopicCrudManager()
DiscussionReplyCrud = DiscussionReplyCrudManager()
DiscussionTopicFileCrud = DiscussionTopicFileCrudManager()
CourseBulletinFileCrud = CourseBulletinFileCrudManager()


async def check_user_id(uid: str):
    user = await UserCrud.get(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    return user.uid


async def check_course_id(course_id: str):
    course = await CourseCrud.get(course_id)
    
    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")
    
    return course.course_id


async def check_website_bulletin_id(wb_id: str):
    website_bulletin = await WebsiteBulletinCrud.get(wb_id)
    if not website_bulletin:
        raise HTTPException(status_code=404, detail="Website bulletin does not exist")
    
    return website_bulletin.wb_id


async def check_website_bulletin_file_id(file_id: str):
    file = await WebsiteBulletinFileCrud.get(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File does not exist")
    
    return file.file_id

async def check_course_bulletin_id(cb_id: str):
    course_bulletin = await CourseBulletinCrud.get(cb_id)
    
    if not course_bulletin:
        raise HTTPException(status_code=404, detail="Bulletin does not exist")
    
    return course_bulletin.cb_id

async def check_course_bulletin_file_id(file_id: str):
    course_bulletin_file = await CourseBulletinFileCrud.get(file_id)
    
    if not course_bulletin_file:
        raise HTTPException(status_code=404, detail="Bulletin file does not exist")
    
    return course_bulletin_file.file_id

async def check_discussion_id(discussion_id: str):
    discussion = await DiscussionCrud.get(discussion_id)
    
    if not discussion:
        raise HTTPException(status_code=404, detail="Discussion does not exist")
    
    return discussion.discussion_id

async def check_discussion_topic_id(topic_id: str):
    discussion_topic = await DiscussionTopicCrud.get(topic_id)
    
    if not discussion_topic:
        raise HTTPException(status_code=404, detail="Discussion topic does not exist")
    
    return discussion_topic.topic_id

async def check_discussion_reply_id(reply_id: str):
    discussion_reply = await DiscussionReplyCrud.get(reply_id)
    
    if not discussion_reply:
        raise HTTPException(status_code=404, detail="Discussion reply does not exist")
    
    return discussion_reply.reply_id

async def check_discussion_topic_file_id(file_id: str):
    discussion_topic_file = await DiscussionTopicFileCrud.get(file_id)
    
    if not discussion_topic_file:
        raise HTTPException(status_code=404, detail="Discussion topic file does not exist")
    
    return discussion_topic_file.file_id
