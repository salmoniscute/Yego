from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_material_info_id, check_user_id, check_course_material_id
from crud.course_material import CourseMaterialCrudManager
from crud.material_info import MaterialInfoCrudManager
from crud.notification import NotificationCrudManager
from crud.selected_course import SelectedCourseCrudManager
from schemas import course_material as CourseMaterialSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Material Info does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Material Info already exists"
)

CourseMaterialCrud = CourseMaterialCrudManager()
MaterialInfoCrud = MaterialInfoCrudManager()
NotificationCrud = NotificationCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
router = APIRouter(
    tags=["Material Info"],
    prefix="/api"
)


@router.post(
    "/material_info", 
    status_code=status.HTTP_201_CREATED
)
async def create_material_info(
    newMaterialInfo: CourseMaterialSchema.MaterialInfoCreate,
    uid: str = Depends(check_user_id),
    course_material_id: int = Depends(check_course_material_id)
):
    material_info = await MaterialInfoCrud.create(uid, course_material_id, newMaterialInfo)

    course_material = await CourseMaterialCrud.get(course_material_id)  
    users = await SelectedCourseCrud.get_by_course_id(course_material[0].course_id)
    for user in users:
        await NotificationCrud.create(user["uid"], material_info.id, "material_info")

    return {"id": material_info.id}


@router.put(
    "/material_info/{material_info_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_material_info(
    newMaterialInfo: CourseMaterialSchema.MaterialInfoUpdate,
    material_info_id: int = Depends(check_material_info_id)
):
    await MaterialInfoCrud.update(material_info_id, newMaterialInfo)

    material_info = await MaterialInfoCrud.get(material_info_id)
    course_material = await CourseMaterialCrud.get(material_info[0].material_id)  
    users = await SelectedCourseCrud.get_by_course_id(course_material[0].course_id)
    for user in users:
        await NotificationCrud.create(user["uid"], material_info[0].id, "material_info")

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