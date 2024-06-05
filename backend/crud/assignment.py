from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from crud.component import ComponentCrudManager
from database.mysql import crud_class_decorator
from models.course_material import Assignment as AssignmentModel
from schemas import course_material as CourseMaterialSchema

ComponentCrud = ComponentCrudManager()


@crud_class_decorator
class AssignmentCrudManager:
    async def create(self, uid: str, material_id: int, newAssignment: CourseMaterialSchema.AssignmentCreate, db_session: AsyncSession):
        # Create component
        obj = {
            "title": newAssignment.title,
            "content": newAssignment.content,
        }
        component = await ComponentCrud.create(uid, obj)
        
        # Create assignment
        assignment = AssignmentModel(
            id=component.id, 
            material_id=material_id,
            submitted_type=newAssignment.submitted_type,
            submitted_object=newAssignment.submitted_object,
            display=newAssignment.display,
            submitted_time=newAssignment.submitted_time,
            deadline=newAssignment.deadline,
            reject_time=newAssignment.reject_time,
            feedback_type=newAssignment.feedback_type,
            order=newAssignment.order
        )
        db_session.add(assignment)
        await db_session.commit()

        return assignment
    
    async def get(self, assignment_id: int, db_session: AsyncSession):
        stmt = select(AssignmentModel).filter(AssignmentModel.id == assignment_id)
        result = await db_session.execute(stmt)
        assignment = result.first()
        
        return assignment
    
    async def update(self, assignment_id: int, newAssignment: CourseMaterialSchema.AssignmentUpdate, db_session: AsyncSession):
        component = {
            "title": newAssignment.title,
            "content": newAssignment.content
        }
        assignment = {
            "display": newAssignment.display
        }

        # Update component
        if component:
            await ComponentCrud.update(assignment_id, component)

        # Update assignment
        if assignment:
            await ComponentCrud.update(assignment_id, component)
            stmt = update(AssignmentModel).where(AssignmentModel.id == assignment_id).values(assignment)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, assignment_id: int, db_session: AsyncSession):
        await ComponentCrud.delete(assignment_id)
        stmt = delete(AssignmentModel).where(AssignmentModel.id == assignment_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
