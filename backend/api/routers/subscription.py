from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_component_id, check_user_id
from crud.subscription import SubscriptionCrudManager
from schemas import subscription as SubscriptionSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Subscription does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Subscription already exists"
)

SubscriptionCrud = SubscriptionCrudManager()
router = APIRouter(
    tags=["Subscriptions"],
    prefix="/api"
)


@router.post(
    "/subscription", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_subscription(
    uid: str = Depends(check_user_id),
    component_id: int = Depends(check_component_id)
):
    """
    Create a subscription.
    """
    if await SubscriptionCrud.get(uid, component_id):
        raise already_exists
    
    subscription = await SubscriptionCrud.create(uid, component_id)

    return subscription
    

@router.delete(
    "/subscription/{uid}/{component_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_subscription(uid: str = Depends(check_user_id), component_id: int = Depends(check_component_id)):
    """
    Delete a subscription.
    """
    await SubscriptionCrud.delete(uid, component_id)

    return
