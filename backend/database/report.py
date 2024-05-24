from datetime import datetime

class Report:
    def __init__(self, fakeDB, component_id_counter):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title": None,
            "content": None
        }
        self.default = {
            "id": None
        }
        self.teacher_list = [user["uid"] for user in fakeDB["users"] if user["role"] == "teacher"]
        self.student_list = [user["uid"] for user in fakeDB["users"] if user["role"] == "student"]
        self.components = fakeDB["components"]
        self.component_id_counter = component_id_counter
        self.results = []
        
    def generate(self):        
        for cnt in range(5):
            self.components.append({
                **self.component_default,
                "uid": self.student_list[cnt] if cnt < 3 else self.teacher_list[cnt - 3],
                "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
                "title": f"問題回報 id = {self.component_id_counter}",
                "content": f"問題回報 id = {self.component_id_counter}"
            })
            self.results.append({
                **self.default,
                "id": self.component_id_counter
            })
            self.component_id_counter += 1

        return self.results, self.component_id_counter
    