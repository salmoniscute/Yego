import random


class Subscription:
    def __init__(self, fakeDB):
        self.default = {
            "uid": None,
            "component_id": None,
        }
        self.user_list = fakeDB["users"]
        self.report_list = fakeDB["reports"]
        self.results = []
        
    def generate(self):
        for user in self.user_list:
            for report in random.sample(self.report_list, 3):
                self.results.append({
                    **self.default, 
                    "uid": user["uid"], 
                    "component_id": report["id"], 
                })
            
        return self.results
    