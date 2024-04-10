from pydantic import BaseModel


class SubscriptionRead(BaseModel):
    uid: str
    component_id: str
