from fastapi import HTTPException

from crud.user import UserCrudManager
from crud.course import CourseCrudManager
from crud.website_bulletin import WebsiteBulletinCrudManager
from crud.website_bulletin_file import WebsiteBulletinFileCrudManager

UserCrud = UserCrudManager()
CourseCrud = CourseCrudManager()
WebsiteBulletinCrud = WebsiteBulletinCrudManager()
WebsiteBulletinFileCrud = WebsiteBulletinFileCrudManager()


async def check_user_id(uid: str):
    user = await UserCrud.get_user_by_id(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    return user.uid


async def check_course_id(course_id: str):
    print(course_id)
    course = await CourseCrud.get_course_by_id(course_id)
    
    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")
    
    return course.course_id


async def check_website_bulletin_id(wb_id: str):
    website_bulletin = await WebsiteBulletinCrud.get_website_bulletin_by_wb_id(wb_id)
    if not website_bulletin:
        raise HTTPException(status_code=404, detail="Website bulletin does not exist")
    
    return website_bulletin.wb_id


async def check_website_bulletin_file_id(file_id: str):
    file = await WebsiteBulletinFileCrud.get_file_by_file_id(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File does not exist")
    
    return file.file_id
