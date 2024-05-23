from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_component_id, check_user_id
from crud.notification import NotificationCrudManager
from schemas import notification as NotificationSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Notification does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Notification already exists"
)

NotificationCrud = NotificationCrudManager()
router = APIRouter(
    tags=["Notification"],
    prefix="/api"
)


@router.put(
    "/notification/particular/{uid}/{component_id}",
    response_model=list[NotificationSchema.NotificationReadByUid],
    status_code=status.HTTP_200_OK
)
async def update_notification(
    uid: str = Depends(check_user_id),
    component_id: int = Depends(check_component_id)
):
    """
    Update a notification.
    """
    notifications = await NotificationCrud.update(uid, component_id)
    if notifications:
        return notifications

    raise not_found

@router.delete(
    "/notification/particular/{uid}/{component_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_notification(uid: str = Depends(check_user_id), component_id: int = Depends(check_component_id)):
    """
    Delete a notification.
    """
    await NotificationCrud.delete(uid, component_id)

    return


@router.get(
    "/notification/user/{uid}",
    response_model=list[NotificationSchema.NotificationReadByUid],
    status_code=status.HTTP_200_OK
)
async def get_notifications_for_one_user(uid: str = Depends(check_user_id)):
    """
    Get all notifications for a user.
    """
    notifications = await NotificationCrud.get_by_uid(uid)
    if notifications:
        return notifications

    raise not_found


@router.put(
    "/notification/user/{uid}/read",
    response_model=list[NotificationSchema.NotificationReadByUid]
)
async def read_notifications_for_one_user(uid: str = Depends(check_user_id)):
    """
    Read all notifications for one user.
    """
    notifications = await NotificationCrud.read_all(uid)
    if notifications:
        return notifications

    raise not_found
