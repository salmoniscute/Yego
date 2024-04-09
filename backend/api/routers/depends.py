from fastapi import HTTPException

from crud.bulletin import CourseBulletinCrudManager, WebsiteBulletinCrudManager
from crud.component import ComponentCrudManager
from crud.course import CourseCrudManager
from crud.discussion import DiscussionCrudManager
from crud.selected_course import SelectedCourseCrudManager
from crud.user import UserCrudManager

ComponentCrud = ComponentCrudManager()
CourseCrud = CourseCrudManager()
CourseBulletinCrud = CourseBulletinCrudManager()
DiscussionCrud = DiscussionCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
UserCrud = UserCrudManager()
WebsiteBulletinCrud = WebsiteBulletinCrudManager()


async def check_user_id(uid: str):
    user = await UserCrud.get(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    return user.uid


async def check_course_id(course_id: str):
    course = await CourseCrud.get(course_id)
    
    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")
    
    return course.id


async def check_component_id(component_id: str):
    component = await ComponentCrud.get(component_id)
    
    if not component:
        raise HTTPException(status_code=404, detail="Component does not exist")
    
    return component.id


async def check_course_bulletin_id(bulletin_id: str):
    bulletin = await CourseBulletinCrud.get(bulletin_id)
    
    if not bulletin:
        raise HTTPException(status_code=404, detail="Course bulletin does not exist")
    
    return bulletin.id


async def check_website_bulletin_id(bulletin_id: str):
    bulletin = await WebsiteBulletinCrud.get(bulletin_id)
    
    if not bulletin:
        raise HTTPException(status_code=404, detail="Website bulletin does not exist")
    
    return bulletin.id

async def check_discussion_id(discussion_id: str):
    discussion = await DiscussionCrud.get(discussion_id)
    
    if not discussion:
        raise HTTPException(status_code=404, detail="Discussion does not exist")
    
    return discussion.id
