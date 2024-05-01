from schemas.component import ComponentCreate, ComponentRead, ComponentUpdate


class ReportCreate(ComponentCreate):    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "1",
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Report 1",
                    "content": "This is the first report."
                }
            ]
        }
    }


class ReportRead(ComponentRead):
    pass

class ReportReplyRead(ComponentRead):
    type: str
    report_id: str
    parent_id: str
    root_id: str

class ReportUpdate(ComponentUpdate):
    pass

