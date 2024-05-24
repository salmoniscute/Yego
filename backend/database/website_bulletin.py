from datetime import datetime


class WebsiteBulletin:
    def __init__(self):
        self.component_default = {
            "uid": "F74102048",
            "release_time": "2024-04-10 16:10:05",
            "title": "網站公告一",
            "content": "這是第一個網站公告"
        }
        self.default = {
            "id": 1,
            "pin_to_top": False
        }
        
        
    def generate(self, components, component_id_counter):
        results = []
        
        count = 5
        for _ in range(count):
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S") 
            data = self.component_default.copy()
            data["uid"] = "admin"
            data["release_time"] = formatted_time
            data["title"] = "網站公告 id = " + str(component_id_counter)
            data["content"] = "網站公告 id = " + str(component_id_counter)
            components.append(data)
            data = self.default.copy()
            data["id"] = component_id_counter
            data["pin_to_top"] = False
            results.append(data)
            component_id_counter += 1
        return results, component_id_counter