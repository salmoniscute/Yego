from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_component_id, check_subscription_id, check_user_id
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
    response_model=SubscriptionSchema.SubscriptionRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_subscription(
    newSubscription: SubscriptionSchema.SubscriptionCreate,
    uid: str = Depends(check_user_id),
    component_id: str = Depends(check_component_id)
):
    """
    Create a subscription with the following information:
    - **id**
    """
    subscription = await SubscriptionCrud.get(newSubscription.id)
    if subscription:
        raise already_exists
    
    subscription = await SubscriptionCrud.create(uid=uid, component_id=component_id, newSubscription=newSubscription)

    return subscription
    

@router.get(
    "/subscriptions",
    response_model=list[SubscriptionSchema.SubscriptionRead],
    status_code=status.HTTP_200_OK
)
async def get_all_subscriptions():
    """ 
    Get all subscriptions.
    """
    subscriptions = await SubscriptionCrud.get_all()
    if not subscriptions:
        raise not_found
    
    return subscriptions


@router.get(
    "/subscription/{subscription_id}",
    response_model=SubscriptionSchema.SubscriptionRead,
    status_code=status.HTTP_200_OK
)
async def get_subscription(subscription_id: str):
    """
    Get a subscription.
    """
    subscription = await SubscriptionCrud.get(subscription_id)
    if not subscription:
        raise not_found
    
    return subscription


@router.delete(
    "/subscription/{subscription_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_subscription(subscription_id: str = Depends(check_subscription_id)):
    """
    Delete a subscription.
    """
    await SubscriptionCrud.delete(subscription_id)

    return
