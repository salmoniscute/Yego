from schemas.component import ComponentCreate, ComponentRead, ComponentUpdate

class DiscussionCreate(ComponentCreate):    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
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


class DiscussionTopicRead(ComponentRead):
    type: str
    discussion_id: int

class DiscussionTopicReplyCreate(DiscussionCreate):
    parent_id: int
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Discussion Topic Reply 1",
                    "content": "This is the first discussion topic reply of the course.",
                    "parent_id": 1
                }
            ]
        }
    }

class DiscussionTopicReplyRead(ComponentRead):
    parent_id: int
    root_id: int


class DiscussionUpdate(ComponentUpdate):
    pass

