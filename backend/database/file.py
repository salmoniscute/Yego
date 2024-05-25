import random


class File:
    def __init__(self, fakeDB):
        self.default = {
            "component_id": None,
            "path": None
        }
        self.reports = fakeDB["reports"]
        self.website_bulletins = fakeDB["website_bulletins"]
        self.course_bulletins = fakeDB["course_bulletins"]
        self.discussion_topics = fakeDB["discussion_topics"]
        self.results = []
        
    def generate(self):
        for report in self.reports + self.website_bulletins + self.course_bulletins + self.discussion_topics:
            self.results.append({
                **self.default,
                "component_id": report["id"],
                "path": random.choice(["/assets/Yego.png", "/assets/Yegogo.png", "/assets/Dago.png"])
            })
        
        return self.results
    