from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.course import Course as CourseModel
from schemas import course as CourseSchema


@crud_class_decorator
class CourseCrudManager:
    async def create(self, uid: str, newCourse: CourseSchema.CourseCreate, db_session: AsyncSession):
        newCourse_dict = newCourse.model_dump()
        course = CourseModel(**newCourse_dict, uid=uid)
        db_session.add(course)
        await db_session.commit()

        return course
     
    async def get(self, course_id: str, db_session: AsyncSession):
        stmt = select(CourseModel).where(CourseModel.id == course_id)
        result = await db_session.execute(stmt)
        result = result.first()
        course = {
            "id": result[0].id,
            "instructor_name": result[0].instructor_info.name,
            "course_code": result[0].course_code,
            "academic_year": result[0].academic_year,
            "semester": result[0].semester,
            "course_name": result[0].name,
            "outline": result[0].outline
        }

        return course

    async def get_all(self, db_session: AsyncSession):
        stmt = select(CourseModel)
        result = await db_session.execute(stmt)
        
        _list = []
        for course in result:
            _list.append({
                "id": course[0].id,
                "instructor_name": course[0].instructor_info.name,
                "course_code": course[0].course_code,
                "academic_year": course[0].academic_year,
                "semester": course[0].semester,
                "course_name": course[0].name,
                "outline": course[0].outline
            })

        return _list
            
    async def update(self, course_id: str, updateCourse: CourseSchema.CourseUpdate, db_session: AsyncSession):
        updateCourse_dict = updateCourse.model_dump(exclude_none=True)
        if updateCourse_dict:
            stmt = update(CourseModel).where(CourseModel.id == course_id).values(**updateCourse_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, course_id: int, db_session: AsyncSession):
        stmt = delete(CourseModel).where(CourseModel.id == course_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    