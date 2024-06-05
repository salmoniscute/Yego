from fastapi import APIRouter, HTTPException, status, Depends

from crud.course_material import CourseMaterialCrudManager
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
    "/update_order",
    status_code=status.HTTP_201_CREATED
)
async def update_order(
    newOrderUpdate: list[OrderUpdateSchema.OrderElement]
):
    """
    Update order of the order elements
    """
    order_element = await CourseMaterialCrud.update_order(newOrderUpdate)
    return {"id": order_element.id}