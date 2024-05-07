from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_material_info_id, check_user_id, check_course_material_id
from crud.material_info import MaterialInfoCrudManager
from schemas import course_material as CourseMaterialSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Material Info does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Material Info already exists"
)

MaterialInfoCrud = MaterialInfoCrudManager()
router = APIRouter(
    tags=["Material Info"],
    prefix="/api"
)

@router.post(
    "/material_info", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_material_info(
    newMaterialInfo: CourseMaterialSchema.MaterialInfoCreate,
    uid: str = Depends(check_user_id),
    course_material_id: int = Depends(check_course_material_id)
):
    material_info = await MaterialInfoCrud.create(uid, course_material_id, newMaterialInfo)

    return material_info

@router.get(
    "/material_info/{material_info_id}", 
    response_model=CourseMaterialSchema.MaterialInfoRead
)
async def get_material_info(
    material_info_id: int 
):
    material_info = await MaterialInfoCrud.get(material_info_id)
    if material_info:
        return material_info
    
    raise not_found

@router.put(
    "/material_info/{material_info_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_material_info(
    newMaterialInfo: CourseMaterialSchema.MaterialInfoUpdate,
    material_info_id: int = Depends(check_material_info_id)
):
    await MaterialInfoCrud.update(material_info_id, newMaterialInfo)

    return

@router.delete(
    "/material_info/{material_info_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_material_info(
    material_info_id: int = Depends(check_material_info_id)
):
    await MaterialInfoCrud.delete(material_info_id)

    return