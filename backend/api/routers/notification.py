from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_user_id, check_notification_id
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
    prefix="/notification"
)


@router.get(
    "/user/{uid}",
    response_model=list[NotificationSchema.NotificationReadByUid],
    status_code=status.HTTP_200_OK
)
async def get_notifications_for_one_user(uid: str = Depends(check_user_id)):
    """
    Get all notifications for a user.
    """
    notifications = await NotificationCrud.get_by_uid(uid)
    if notifications:
        notifications.reverse()
        return notifications

    raise not_found

@router.put(
    "/read/{uid}/{notification_id}",
    response_model=list[NotificationSchema.NotificationReadByUid],
    status_code=status.HTTP_200_OK
)
async def read_one_notification(
    uid: str = Depends(check_user_id),
    notification_id: int = Depends(check_notification_id)
):
    """
    Read a notification.
    """
    notifications = await NotificationCrud.update(uid, notification_id)
    if notifications:
        notifications.reverse()
        return notifications

    raise not_found


@router.put(
    "/read/{uid}",
    response_model=list[NotificationSchema.NotificationReadByUid]
)
async def read_notifications_for_one_user(uid: str = Depends(check_user_id)):
    """
    Read all notifications for one user.
    """
    notifications = await NotificationCrud.read_all(uid)
    if notifications:
        notifications.reverse()
        return notifications

    raise not_found


@router.delete(
    "/particular/{notification_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_notification(
    notification_id: int = Depends(check_notification_id)
):
    """
    Delete a notification.
    """
    await NotificationCrud.delete(notification_id)

    return
