# from sqlalchemy import select, update, delete
# from sqlalchemy.ext.asyncio import AsyncSession

# from crud.component import ComponentCrudManager
# from database.mysql import crud_class_decorator
# from models.component import Component as ComponentModel
# from models.course_material import CourseMaterial as CourseMaterialModel, MaterialInfo as MaterialInfoModel, SubmittedAssignment as SubmittedAssignmentModel
# from schemas import course_material as CourseMaterialSchema

# ComponentCrud = ComponentCrudManager()

# @crud_class_decorator
# class SubmittedAssignmentCrudManager:
#     async def create(self, uid:str, material_info_id:int, grade:int, newSubmittedMaterial:CourseMaterialSchema.SubmittedMaterialCreate, db_session:AsyncSession):
#         newComponent_dict = newSubmittedMaterial.model_dump()
#         component = await ComponentCrud.create(uid, newComponent_dict)
        
#         submitted_material = SubmittedAssignmentModel(id = component.id, assignment_id = material_info_id, grade = grade)
#         db_session.add(submitted_material)
#         await db_session.commit()
        
#         return submitted_material
    
#     async def get(self, submitted_assignment_id:int, db_session:AsyncSession):
#         stmt = select(SubmittedAssignmentModel).where(SubmittedAssignmentModel.id == submitted_assignment_id)
#         result = await db_session.execute(stmt)
#         submitted_assignment = result.first()
#         obj = {}
#         if submitted_assignment:
#             await db_session.refresh(submitted_assignment[0], ["info"])
#             obj = {
#                 "id": submitted_assignment[0].id,
#                 "uid": submitted_assignment[0].info.uid,
#                 "assignment_id": submitted_assignment[0].assignment_id,
#                 "grade": submitted_assignment[0].grade,
#                 "title": submitted_assignment[0].info.title,
#                 "content": submitted_assignment[0].info.content
#             }
#         return obj
    
#     async def update(self, submitted_assignment_id:int, newSubmittedMaterial:CourseMaterialSchema.SubmittedMaterialUpdate, db_session:AsyncSession):
#         updateSubmittedSubmitted_dict = newSubmittedMaterial.model_dump(exclude_none=True)
#         component = {
#             "title": updateSubmittedSubmitted_dict["title"],
#             "content": updateSubmittedSubmitted_dict["content"]
#         }
#         submitted_assignment = {
#             "grade": updateSubmittedSubmitted_dict["grade"]
#         }
#         if updateSubmittedSubmitted_dict:
#             await ComponentCrud.update(submitted_assignment_id, component)
#             stmt = update(SubmittedAssignmentModel).where(SubmittedAssignmentModel.id == submitted_assignment_id).values(submitted_assignment)
#             await db_session.execute(stmt)
#             await db_session.commit()
        
#         return
    
#     async def delete(self, submitted_assignment_id:int, db_session:AsyncSession):
#         stmt = delete(ComponentModel).where(ComponentModel.id == submitted_assignment_id)
#         await db_session.execute(stmt)
#         await db_session.commit()
        
#         return