from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_component_id, check_course_id, check_user_id
from crud.course_material import CourseMaterialCrudManager
from schemas import course_material as CourseMaterialSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Course material does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Course material already exists"
)

CourseMaterialCrud = CourseMaterialCrudManager()
router = APIRouter(
    tags=["Course Material"],
    prefix="/api"
)

@router.post(
    "/course_material", 
    response_model=CourseMaterialSchema.CourseMaterialCreate,
    status_code=status.HTTP_201_CREATED
)
async def create_course_material(
    newCourseMaterial: CourseMaterialSchema.CourseMaterialCreate,
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """
    Create a course material with the following information:
    - **release_time**
    - **title**
    - **content**
    """
    course_material = await CourseMaterialCrud.create(uid, course_id, newCourseMaterial)

    return course_material


@router.get(
    "/course_materials",
    response_model=list[CourseMaterialSchema.CourseMaterialRead]
)
async def get_all_course_materials():
    """ 
    Get all course materials.
    """
    course_materials = await CourseMaterialCrud.get_all()
    if course_materials:
        return course_materials
    
    raise not_found


@router.get(
    "/course_material/{course_material_id}", 
    response_model=CourseMaterialSchema.CourseMaterialRead
)
async def get_course_material(course_material_id: str):
    course_material = await CourseMaterialCrud.get(course_material_id)
    if course_material:
        return course_material
    
    raise not_found

@router.put(
    "/course_material/{course_material_id}",
    response_model=CourseMaterialSchema.CourseMaterialUpdate
)
async def update_course_material(
    course_material_id: str,
    updateCourseMaterial: CourseMaterialSchema.CourseMaterialUpdate
):
    course_material = await CourseMaterialCrud.update(course_material_id, updateCourseMaterial)
    if course_material:
        return course_material
    
    raise not_found

@router.delete(
    "/course_material/{course_material_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course_material(course_material_id: str):
    await CourseMaterialCrud.delete(course_material_id)
    
    return