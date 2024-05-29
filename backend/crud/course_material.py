from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from crud.component import ComponentCrudManager
from models.component import Component as ComponentModel
from models.course_material import CourseMaterial as CourseMaterialModel, MaterialInfo as MaterialInfoModel
from schemas import course_material as CourseMaterialSchema

ComponentCrud = ComponentCrudManager()


@crud_class_decorator
class CourseMaterialCrudManager:
    async def create(self, uid: str, course_id: int, newCourseMaterial: CourseMaterialSchema.CourseMaterialCreate, db_session: AsyncSession):
        newComponent_dict = newCourseMaterial.model_dump()
        newComponent_dict.update({"content": "(empty_content)"})
        component = await ComponentCrud.create(uid, newComponent_dict)
        
        course_material = CourseMaterialModel(id=component.id, course_id=course_id)
        db_session.add(course_material)
        await db_session.commit()

        return course_material
    
    async def get(self, course_material_id: int, db_session: AsyncSession):
        stmt = select(CourseMaterialModel).where(CourseMaterialModel.id == course_material_id)
        result = await db_session.execute(stmt)
        course_material = result.first()
        print(course_material)

        return course_material
    
    async def get_all_in_particular_course(self, course_id: int, db_session: AsyncSession):
        stmt = select(CourseMaterialModel).where(CourseMaterialModel.course_id == course_id)
        result = await db_session.execute(stmt)
        result = result.unique()

        _list = []
        for material in result:
            await db_session.refresh(material[0], ["info"])
            stmt = select(MaterialInfoModel).where(MaterialInfoModel.material_id == material[0].id)
            infos = await db_session.execute(stmt)
            obj = {
                "id": material[0].id,
                "title": material[0].info.title,
                "material_infos": []
            }
            for info in infos:
                await db_session.refresh(info[0], ["info"])
                obj["material_infos"].append({
                    "id": info[0].id,
                    "title": info[0].info.title,
                    "content": info[0].info.content,
                    "start_time": info[0].start_time,
                    "end_time": info[0].end_time,
                    "display": info[0].display,
                    "files": info[0].info.files
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
