from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_course_id, check_user_id, check_course_material_id
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
    status_code=status.HTTP_201_CREATED
)
async def create_course_material(
    newCourseMaterial: CourseMaterialSchema.CourseMaterialCreate,
    uid: str = Depends(check_user_id),
    course_id: int = Depends(check_course_id)
):
    """
    Create a course material with the following information:
    - **title**
    """
    course_material = await CourseMaterialCrud.create(uid, course_id, newCourseMaterial)

    return {"id": course_material.id}


@router.get(
    "/course_material/particular_course/{course_id}",
    response_model=list[CourseMaterialSchema.CourseMaterialRead]
)
async def get_all_course_materials_in_particular_course(
    course_id: int = Depends(check_course_id)
):
    """ 
    Get all course materials in particular course.
    """
    course_materials = await CourseMaterialCrud.get_all_in_particular_course(course_id)
    if course_materials:
        return course_materials
    
    raise not_found


@router.put(
    "/course_material/{course_material_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course_material(
    updateCourseMaterial: CourseMaterialSchema.CourseMaterialUpdate,
    course_material_id: int = Depends(check_course_material_id)
):
    await CourseMaterialCrud.update(course_material_id, updateCourseMaterial)
    return 


@router.delete(
    "/course_material/{course_material_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course_material(course_material_id: int = Depends(check_course_material_id)):
    await CourseMaterialCrud.delete(course_material_id)
    return
