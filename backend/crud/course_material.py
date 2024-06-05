from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from crud.component import ComponentCrudManager
from models.component import Component as ComponentModel
from models.course_material import CourseMaterial as CourseMaterialModel, MaterialInfo as MaterialInfoModel, Assignment as AssignmentModel
from schemas import course_material as CourseMaterialSchema

ComponentCrud = ComponentCrudManager()


@crud_class_decorator
class CourseMaterialCrudManager:
    async def create(self, uid: str, course_id: int, newCourseMaterial: CourseMaterialSchema.CourseMaterialCreate, db_session: AsyncSession):
        stmt = select(CourseMaterialModel).where(CourseMaterialModel.course_id == course_id)
        result = await db_session.execute(stmt)
        course_material_list = [course_material[0].order for course_material in result.all()]
        order = max(course_material_list) + 1 if course_material_list else 1

        newComponent_dict = {
            "title": newCourseMaterial.title,
            "content": "(empty_content)"
        }
        component = await ComponentCrud.create(uid, newComponent_dict)
        
        course_material = CourseMaterialModel(id=component.id, course_id=course_id, order=order)
        db_session.add(course_material)
        await db_session.commit()

        return course_material
    
    async def get(self, course_material_id: int, db_session: AsyncSession):
        stmt = select(CourseMaterialModel).where(CourseMaterialModel.id == course_material_id)
        result = await db_session.execute(stmt)
        course_material = result.first()

        return course_material
    
    async def get_all_in_particular_course(self, course_id: int, db_session: AsyncSession):
        stmt = select(CourseMaterialModel).where(CourseMaterialModel.course_id == course_id)
        result = await db_session.execute(stmt)
        result = result.unique()

        _list = []
        for material in result:
            await db_session.refresh(material[0], ["info"])
            obj = {
                "id": material[0].id,
                "title": material[0].info.title,
                "order": material[0].order,
                "material_infos": [],
                "assignments": []
            }

            stmt = select(MaterialInfoModel).where(MaterialInfoModel.material_id == material[0].id)
            infos = await db_session.execute(stmt)
            for info in infos:
                await db_session.refresh(info[0], ["info"])
                obj["material_infos"].append({
                    "id": info[0].id,
                    "title": info[0].info.title,
                    "content": info[0].info.content,
                    "start_time": info[0].start_time,
                    "end_time": info[0].end_time,
                    "display": info[0].display,
                    "order": info[0].order,
                    "files": info[0].info.files
                })

            stmt = select(AssignmentModel).where(AssignmentModel.material_id == material[0].id)
            assignments = await db_session.execute(stmt)
            for assignment in assignments:
                await db_session.refresh(assignment[0], ["info"])
                obj["assignments"].append({
                    "id": assignment[0].id,
                    "title": assignment[0].info.title,
                    "content": assignment[0].info.content,
                    "submitted_type": assignment[0].submitted_type,
                    "submitted_object": assignment[0].submitted_object,
                    "display": assignment[0].display,
                    "submitted_time": assignment[0].submitted_time,
                    "deadline": assignment[0].deadline,
                    "reject_time": assignment[0].reject_time,
                    "feedback_type": assignment[0].feedback_type,
                    "order": assignment[0].order,
                    "files": assignment[0].info.files
                })
                
            _list.append(obj)
        
        return _list
    
    async def update(self, course_material_id: str, updateCourseMaterial: CourseMaterialSchema.CourseMaterialUpdate, db_session: AsyncSession):
        updateCourseMaterial_dict = updateCourseMaterial.model_dump(exclude_none=True)
        if updateCourseMaterial_dict:
            stmt = update(ComponentModel).where(ComponentModel.id == course_material_id).values(**updateCourseMaterial_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, course_material_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == course_material_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
