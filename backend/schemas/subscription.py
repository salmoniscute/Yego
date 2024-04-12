from pydantic import BaseModel


class SubscriptionCreate(BaseModel):
    type: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "type": "website_bulletin"
                }
            ]
        }
    }

class SubscriptionRead(BaseModel):
    id: int
    uid: str
    component_id: int
    type: str
