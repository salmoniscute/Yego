from pydantic import BaseModel


class SubscriptionCreate(BaseModel):
    id: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "id": "1"
                }
            ]
        }
    }


class SubscriptionRead(BaseModel):
    id: str
    uid: str
    component_id: str
