# from fastapi import APIRouter, HTTPException, status, Depends

# from .depends import check_submitted_assignment_id, check_material_info_id, check_user_id
# from crud.submitted_assignment import SubmittedAssignmentCrudManager
# from schemas import course_material as CourseMaterialSchema

# not_found = HTTPException(
#     status_code=status.HTTP_404_NOT_FOUND, 
#     detail="Submitted Assignment does not exist"
# )

# already_exists = HTTPException(
#     status_code=status.HTTP_409_CONFLICT, 
#     detail="Submitted Assignment already exists"
# )

# SubmittedMaterialCrud = SubmittedAssignmentCrudManager()
# router = APIRouter(
#     tags=["Submitted Assignment"],
#     prefix="/api"
# )

# @router.post(
#     "/submitted_assignment",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def create_submitted_assignment(
#     newSubmittedMaterial: CourseMaterialSchema.SubmittedMaterialCreate,
#     grade: int,
#     uid: str = Depends(check_user_id),
#     material_info_id: int = Depends(check_material_info_id),
# ):
#     """
#     Create a submitted assignment with the following information:
#     - **release_time**
#     - **title**
#     - **content**
#     """
#     submitted_material = await SubmittedMaterialCrud.create(uid, material_info_id, grade, newSubmittedMaterial)

#     return submitted_material

# @router.get(
#     "/submitted_assignment/{submitted_assignment_id}", 
#     response_model=CourseMaterialSchema.SubmittedMaterialRead
# )
# async def get_submitted_assignment(
#     submitted_assignment_id: int = Depends(check_submitted_assignment_id)
# ):
#     """ 
#     Get a submitted assignment by its id.
#     """
#     submitted_material = await SubmittedMaterialCrud.get(submitted_assignment_id)
#     if submitted_material:
#         return submitted_material
    
#     raise not_found

# @router.put(
#     "/submitted_assignment/{submitted_assignment_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def update_submitted_assignment(
#     update: CourseMaterialSchema.SubmittedMaterialUpdate,
#     submitted_assignment_id: int = Depends(check_submitted_assignment_id)
# ):
#     """
#     Update a submitted assignment by its id.
#     """
#     await SubmittedMaterialCrud.update(submitted_assignment_id, update)
    
#     return

# @router.delete(
#     "/submitted_assignment/{submitted_assignment_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def delete_submitted_assignment(
#     submitted_assignment_id: int = Depends(check_submitted_assignment_id)
# ):
#     """
#     Delete a submitted assignment by its id.
#     """
#     await SubmittedMaterialCrud.delete(submitted_assignment_id)
    
#     return