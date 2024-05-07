from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from crud.component import ComponentCrudManager
from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel
from models.course_material import CourseMaterial as CourseMaterialModel, MaterialInfo as MaterialInfoModel
from schemas import course_material as CourseMaterialSchema

ComponentCrud = ComponentCrudManager()

@crud_class_decorator
class MaterialInfoCrudManager:
    async def create(self, uid: str, course_material_id: int, newMaterialInfo: CourseMaterialSchema.MaterialInfoCreate, db_session: AsyncSession):
        newComponent_dict = newMaterialInfo.model_dump()
        obj = {
            "title": newComponent_dict["title"],
            "content": newComponent_dict["content"],
            "release_time": newComponent_dict["release_time"],
        }
        component = await ComponentCrud.create(uid, obj)
        
        material_info = MaterialInfoModel(id=component.id, material_id=course_material_id, type=newComponent_dict["type"], start_time=newComponent_dict["start_time"], end_time=newComponent_dict["end_time"], assignment_reject_time=newComponent_dict["assignment_reject_time"], display=newComponent_dict["display"])
        db_session.add(material_info)
        await db_session.commit()

        return material_info
    
    async def get(self, material_info_id: int, db_session: AsyncSession):
        stmt = select(MaterialInfoModel).filter(MaterialInfoModel.id == material_info_id)
        result = await db_session.execute(stmt)
        material_info = result.first()
        obj = {}
        if material_info:
            await db_session.refresh(material_info[0], ["info"])
            obj = {
                "id": material_info[0].id,
                "uid": material_info[0].info.uid,
                "title": material_info[0].info.title,
                "content": material_info[0].info.content,
                "release_time": material_info[0].info.release_time,
                "type": material_info[0].type,
                "start_time": material_info[0].start_time,
                "end_time": material_info[0].end_time,
                "assignment_reject_time": material_info[0].assignment_reject_time,
                "display": material_info[0].display
            }
        
        return obj
    
    async def update(self, material_info_id: int, newMaterialInfo: CourseMaterialSchema.MaterialInfoUpdate, db_session: AsyncSession):
        updateMaterialInfo_dict = newMaterialInfo.model_dump()
        component = {
            "title": updateMaterialInfo_dict["title"],
            "content": updateMaterialInfo_dict["content"]
        }
        material_info = {
            "type": updateMaterialInfo_dict["type"],
            "start_time": updateMaterialInfo_dict["start_time"],
            "end_time": updateMaterialInfo_dict["end_time"],
            "assignment_reject_time": updateMaterialInfo_dict["assignment_reject_time"],
            "display": updateMaterialInfo_dict["display"]
        }
        if updateMaterialInfo_dict:
            await ComponentCrud.update(material_info_id, component)
            stmt = update(MaterialInfoModel).where(MaterialInfoModel.id == material_info_id).values(material_info)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, material_info_id: int, db_session: AsyncSession):
        await ComponentCrud.delete(material_info_id)
        stmt = delete(MaterialInfoModel).where(MaterialInfoModel.id == material_info_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return