from typing import Optional

from schemas.component import ComponentCreate, ComponentRead, ComponentUpdate


class DiscussionCreate(ComponentCreate):    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "D001",
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Discussion 1",
                    "content": "This is the first discussion of the course."
                }
            ]
        }
    }


class DiscussionRead(ComponentRead):
    pass
    # topics: Optional[list[DiscussionTopicRead]] = None
    

class DiscussionUpdate(ComponentUpdate):
    pass
