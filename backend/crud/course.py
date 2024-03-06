from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.course import Course as CourseModel
from schemas import course as CourseSchema

@crud_class_decorator
class CourseCrudManager:
    async def create_course(self, newCourse: CourseSchema.CourseCreate, db_session: AsyncSession):
        course = CourseModel(
            course_id = newCourse.course_id,
            teacher = newCourse.teacher,
            course_code = newCourse.course_code,
            academic_year = newCourse.academic_year,
            semester = newCourse.semester,
            name = newCourse.name,
            outline = newCourse.outline
        )
        db_session.add(course)
        await db_session.commit()
        db_session.refresh(course)

        return course

    async def get_course_by_id(self, course_id: str, db_session: AsyncSession):
        print("before select")
        stmt = select(
            CourseModel.course_id,
            CourseModel.teacher,
            CourseModel.course_code,
            CourseModel.academic_year,
            CourseModel.semester,
            CourseModel.name,
            CourseModel.outline
        ).where(CourseModel.course_id == course_id)
        result = await db_session.execute(stmt)
        course = result.first()
        print("after select")
        if course:
            return course
        
        return None

    async def update_course_by_id(self, course_id: str, updateCourse: CourseSchema.CourseUpdate, db_session: AsyncSession):
        stmt = update(CourseModel).where(CourseModel.course_id == course_id).values(
            teacher=updateCourse.teacher,
            course_code=updateCourse.course_code,
            academic_year=updateCourse.academic_year,
            semester=updateCourse.semester,
            name=updateCourse.name,
            outline=updateCourse.outline
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_course_by_id(self, course_id: int, db_session: AsyncSession):
        stmt = delete(CourseModel).where(CourseModel.course_id == course_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    