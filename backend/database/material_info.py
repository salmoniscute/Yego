import random
from datetime import datetime


class MaterialInfo:
    def __init__(self, fakeDB, component_id_counter):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title": None,
            "content": None
        }
        self.default = {
            "id": None,
            "material_id": None,
            "start_time": None,
            "end_time": None,
            "display": None
        }
        self.course_list = fakeDB["courses"]
        self.course_material_list = fakeDB["course_materials"]
        self.components = fakeDB["components"]
        self.component_id_counter = component_id_counter
        self.results = []
        
    def generate(self):
        for course_material in self.course_material_list:
            for _ in range(random.choice([3, 4, 5])):
                teacher = None
                for course in self.course_list:
                    teacher = course["uid"] if course["id"] == course_material["course_id"] else None
                    if teacher:
                        break
                self.components.append({
                    **self.component_default,
                    "uid": teacher,
                    "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
                    "title": f"教材檔案 title = {self.component_id_counter}",
                    "content": f"教材檔案 content "
                })
                self.results.append({
                    **self.default,
                    "id": self.component_id_counter,
                    "material_id": course_material["id"],
                    "start_time": "2024-04-12T12:34:56",
                    "end_time": "2024-04-12T12:34:56",
                    "display": random.choice([True, False])
                })
                self.component_id_counter += 1

        return self.results, self.component_id_counter
