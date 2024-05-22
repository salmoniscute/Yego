from datetime import datetime

class Report:
    def __init__(self, fakeDB):
        self.component_default = {
            "uid": "F74102048",
            "release_time": "2024-04-10 16:10:05",
            "title": "網站公告一",
            "content": "這是第一個網站公告"
        }
        self.default = {
            "id": 8
        }
        self.teacher_list = [user["uid"] for user in fakeDB["users"] if user["role"] == "teacher"]
        self.student_list = [user["uid"] for user in fakeDB["users"] if user["role"] == "student"]
        
    def generate(self, components, component_id_counter):
        results = []
        
        count = 5
        for cnt in range(count):
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S") 
            data = self.component_default.copy()
            if cnt < 3:
                data["uid"] = self.student_list[cnt]
            else:
                data["uid"] = self.teacher_list[cnt-3]
            data["release_time"] = formatted_time
            data["title"] = "問題回報 id = " + str(component_id_counter)
            data["content"] = "問題回報 id = " + str(component_id_counter)
            components.append(data)
            data = self.default.copy()
            data["id"] = component_id_counter
            results.append(data)
            component_id_counter += 1
        return results, component_id_counter