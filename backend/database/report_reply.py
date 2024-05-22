from datetime import datetime

class ReportReply:
    def __init__(self, fakeDB):
        self.component_default = {
            "uid": "F74102048",
            "release_time": "2024-04-10 16:10:05",
            "title" : "None",
            "content": "這是第一個網站公告回覆"
        }
        self.default = {
            "id":1,
            "root_id": 2,
            "parent_id": 0
        }
        self.student_list = [user["uid"] for user in fakeDB["users"] if user["role"] == "student"]
        self.report_list = [component["id"] for component in fakeDB["reports"]]
        
    def generate(self, components, component_id_counter):
        results = []
        
        
        for report in range(5):
            for reply in range(10):
                if reply %5 == 0:
                    parent = component_id_counter
                current_time = datetime.now()
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S") 
                data = self.component_default.copy()
                data["uid"] = self.student_list[5*report + reply]
                data["release_time"] = formatted_time
                data["content"] = "問題回報回覆 id = " + str(component_id_counter)
                components.append(data)
                data = self.default.copy()
                data["id"] = component_id_counter
                data["root_id"] = self.report_list[report]
                if reply %5 != 0:
                    data["parent_id"] = parent
                results.append(data)
                component_id_counter += 1
        return results, component_id_counter