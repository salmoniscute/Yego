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


@router.post(
    "/notification", 
    status_code=status.HTTP_204_NO_CONTENT,
    deprecated=True
)
async def create_notification(
    newNotification: NotificationSchema.NotificationCreate,
    uid: str = Depends(check_user_id),
    component_id: int = Depends(check_component_id)
):
    """
    Create a notification with the following information:
    - **have_read**
    - **release_time**
    """
    if await NotificationCrud.get(uid, component_id):
        raise already_exists
    
    notification = await NotificationCrud.create(uid, component_id, newNotification)

    return notification
    

@router.get(
    "/notification/all",
    response_model=list[NotificationSchema.NotificationRead],
    status_code=status.HTTP_200_OK,
    deprecated=True
)
async def get_all_notifications():
    """ 
    Get all notifications.
    """
    notifications = await NotificationCrud.get_all()
    if not notifications:
        raise not_found
    
    return notifications


@router.get(
    "/notification/particular/{uid}/{component_id}",
    response_model=NotificationSchema.NotificationRead,
    status_code=status.HTTP_200_OK,
    deprecated=True
)
async def get_notification(uid: str, component_id: int):
    """
    Get a notification.
    """
    notification = await NotificationCrud.get(uid, component_id)
    if not notification:
        raise not_found
    
    return notification


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
