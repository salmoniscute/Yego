from fastapi import HTTPException

from crud.user import UserCrudManager
from crud.course import CourseCrudManager

UserCrud = UserCrudManager()
CourseCrud = CourseCrudManager()


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