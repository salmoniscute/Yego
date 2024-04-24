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
    response_model=NotificationSchema.NotificationRead,
    status_code=status.HTTP_201_CREATED
)
async def create_notification(
    newNotification: NotificationSchema.NotificationCreate,
    uid: str = Depends(check_user_id),
    component_id: str = Depends(check_component_id)
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
    status_code=status.HTTP_200_OK
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
    status_code=status.HTTP_200_OK
)
async def get_notification(uid: str, component_id: str):
    """
    Get a notification.
    """
    notification = await NotificationCrud.get(uid, component_id)
    if not notification:
        raise not_found
    
    return notification


@router.put(
    "/notification/particular/{uid}/{component_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_notification(
    updateNotification: NotificationSchema.NotificationUpdate,
    uid: str = Depends(check_user_id),
    component_id: str = Depends(check_component_id)
):
    """
    Update a notification.
    """
    await NotificationCrud.update(uid, component_id, updateNotification)

    return


@router.delete(
    "/notification/particular/{uid}/{component_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_notification(uid: str = Depends(check_user_id), component_id: str = Depends(check_component_id)):
    """
    Delete a notification.
    """
    await NotificationCrud.delete(uid, check_component_id)

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
    results= []

    notifications = await NotificationCrud.get_by_uid(uid)
    if notifications:
        for notification in notifications:
            results.append({
                "id": notification.id,
                "publisher": notification.user_info.name,
                # "course_name": notification.component_info.course_name,
                "course_name": "(TODO)",
                "release_time": notification.release_time,
                "title": notification.component_info.title,
                "content": notification.component_info.content,
                "have_read": notification.have_read,
                "icon_type": notification.type
            })
        return results

    raise not_found


@router.put(
    "/notification/user/{uid}/read",
    response_model=list[NotificationSchema.NotificationReadByUid]
)
async def read_notifications_for_one_user(uid: str = Depends(check_user_id)):
    """
    Read all notifications for one user.
    """
    results = []
    notifications = await NotificationCrud.read_all(uid)
    if notifications:
        for notification in notifications:
            results.append({
                "id": notification.id,
                "publisher": notification.user_info.name,
                # "course_name": notification.component_info.course_name,
                "course_name": "(TODO)",
                "release_time": notification.release_time,
                "title": notification.component_info.title,
                "content": notification.component_info.content,
                "have_read": notification.have_read,
                "icon_type": notification.type
            })
        return results

    raise not_found
