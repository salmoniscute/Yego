from pydantic import BaseModel


class SubscriptionRead(BaseModel):
    id: int
    uid: str
    component_id: int
