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
    uid: str
    component_id: str
    type: str
