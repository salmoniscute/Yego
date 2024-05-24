from datetime import datetime


class WebsiteBulletin:
    def __init__(self, fakeDB, component_id_counter):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title": None,
            "content": None
        }
        self.default = {
            "id": None,
            "pin_to_top": None
        }
        self.components = fakeDB["components"]
        self.component_id_counter = component_id_counter
        self.results = []
        
    def generate(self):        
        for _ in range(5):
            self.components.append({
                **self.component_default,
                "uid": "admin",
                "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "title": f"網站公告 id = {self.component_id_counter}",
                "content": f"網站公告 id = {self.component_id_counter}"
            })
            self.results.append({
                **self.default,
                "id": self.component_id_counter,
                "pin_to_top": False
            })
            self.component_id_counter += 1

        return self.results, self.component_id_counter
