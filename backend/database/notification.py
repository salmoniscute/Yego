import random
from datetime import datetime


class Notification:
    def __init__(self, fakeDB):
        self.default = {
            "uid": None,
            "component_id": None,
            "have_read": False,
            "release_time": None,
            "type": None
        }
        self.user_list = fakeDB["users"]
        self.component_list = fakeDB["components"]
        self.selected_course_list = fakeDB["selected_courses"]
        self.report_list = fakeDB["reports"]
        self.course_bulletin_list = fakeDB["course_bulletins"]
        self.discussion_list = fakeDB["discussions"]
        self.discussion_topic_list = fakeDB["discussion_topics"] 
        self.results = []
        
    def generate(self):
        for user in self.user_list:
            for report in random.sample(self.report_list, 3):
                self.results.append({
                    **self.default, 
                    "uid": user["uid"], 
                    "component_id": report["id"], 
                    "have_read": False,
                    "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                    "type": "report"
                })
            
        return self.results
    