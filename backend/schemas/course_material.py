from schemas.component import ComponentCreate, ComponentRead, ComponentUpdate


class CourseMaterialCreate(ComponentCreate):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Course Material 1",
                    "content": "This is the first course material of the course."
                }
            ]
        }
    }
    

class CourseMaterialRead(ComponentRead):
    pass


class CourseMaterialUpdate(ComponentUpdate):
    pass
