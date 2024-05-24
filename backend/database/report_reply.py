from datetime import datetime

class ReportReply:
    def __init__(self, fakeDB, component_id_counter):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title" : None,
            "content": None
        }
        self.default = {
            "id": None,
            "root_id": None,
            "parent_id": None
        }
        self.student_list = [user["uid"] for user in fakeDB["users"] if user["role"] == "student"]
        self.report_list = [component["id"] for component in fakeDB["reports"]]
        self.components = fakeDB["components"]
        self.component_id_counter = component_id_counter
        self.results = []
        
    def generate(self):
        for report in range(5):
            for reply in range(10):
                if reply % 5 == 0:
                    parent = self.component_id_counter
                self.components.append({
                    **self.component_default,
                    "uid": self.student_list[5 * report + reply],
                    "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
                    "title": f"問題回報回覆 id = {self.component_id_counter}",
                    "content": f"問題回報回覆 id = {self.component_id_counter}"
                })
                self.results.append({
                    **self.default,
                    "id": self.component_id_counter,
                    "root_id": self.report_list[report],
                    "parent_id": parent if reply % 5 != 0 else 0
                })
                self.component_id_counter += 1

        return self.results, self.component_id_counter
    