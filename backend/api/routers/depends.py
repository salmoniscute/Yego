from fastapi import HTTPException

from crud.course import CourseCrudManager
from crud.selected_course import SelectedCourseCrudManager
from crud.user import UserCrudManager
from crud.component import ComponentCrudManager
from crud.course_bulletin import CourseBulletinCrudManager

CourseCrud = CourseCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
UserCrud = UserCrudManager()
ComponentCrud = ComponentCrudManager()
CourseBulletinCrud = CourseBulletinCrudManager()


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
