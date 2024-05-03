from fastapi import HTTPException, status

from crud.component import ComponentCrudManager
from crud.course import CourseCrudManager
from crud.course_bulletin import CourseBulletinCrudManager
from crud.discussion import DiscussionCrudManager
from crud.selected_course import SelectedCourseCrudManager
from crud.user import UserCrudManager
from crud.website_bulletin import WebsiteBulletinCrudManager
from crud.report import ReportCrudManager
from crud.report_reply import ReportReplyCrudManager

ComponentCrud = ComponentCrudManager()
CourseCrud = CourseCrudManager()
CourseBulletinCrud = CourseBulletinCrudManager()
DiscussionCrud = DiscussionCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
UserCrud = UserCrudManager()
WebsiteBulletinCrud = WebsiteBulletinCrudManager()
ReportCrud = ReportCrudManager()
ReportReplyCrud = ReportReplyCrudManager()


async def check_user_id(uid: str):
    user = await UserCrud.get(uid)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    return uid


async def check_course_id(course_id: str):
    course = await CourseCrud.get(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course does not exist")
    
    return course_id


async def check_component_id(component_id: int):
    component = await ComponentCrud.get(component_id)
    if not component:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Component does not exist")
    
    return component_id


async def check_course_bulletin_id(course_bulletin_id: int):
    bulletin = await CourseBulletinCrud.get(course_bulletin_id)
    if not bulletin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course bulletin does not exist")
    
    return course_bulletin_id


async def check_website_bulletin_id(website_bulletin_id: int):
    bulletin = await WebsiteBulletinCrud.get(website_bulletin_id)
    if not bulletin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Website bulletin does not exist")
    
    return website_bulletin_id

async def check_report_id(report_id: int):
    report = await ReportCrud.get(report_id)
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report does not exist")
    
    return report_id


async def check_reply_id(reply_id: int):
    if reply_id == 0:
        return reply_id
    
    reply = await ReportReplyCrud.get(reply_id)
    if not reply:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report reply does not exist")
    
    return reply_id
