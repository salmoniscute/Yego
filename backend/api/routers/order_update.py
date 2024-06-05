from fastapi import APIRouter, HTTPException, status, Depends
from .depends import check_course_material_id

from crud.course_material import CourseMaterialCrudManager
from crud.material_info import MaterialInfoCrudManager
from schemas import order_update as OrderUpdateSchema


not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Notification does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Notification already exists"
)

CourseMaterialCrud = CourseMaterialCrudManager()
router = APIRouter(
    tags=["Order Update"],
    prefix="/order_update"
)

@router.post(
    "/update_order/course_material",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course_material_order(
    newOrderUpdate: list[OrderUpdateSchema.OrderElement]
):
    """
    Update order of the order elements
    """
    await CourseMaterialCrud.update_course_material_order(newOrderUpdate)
    return

@router.post(
    "/update_order/material_info_and_assignment",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_material_info_and_assignment_order(
    newOrderUpdate: list[OrderUpdateSchema.OrderElement]
):
    """
    Update order of the order elements
    """
    await CourseMaterialCrud.update_material_assignment_order(newOrderUpdate)
    return