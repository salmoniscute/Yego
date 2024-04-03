from fastapi import HTTPException

from crud.course import CourseCrudManager
from crud.selected_course import SelectedCourseCrudManager
from crud.user import UserCrudManager

CourseCrud = CourseCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
UserCrud = UserCrudManager()


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
