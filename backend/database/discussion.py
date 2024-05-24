from datetime import datetime


class Discussion:
    def __init__(self, fakeDB, component_id_counter):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title": None,
            "content": None
        }
        self.default = {
            "id": None,
            "course_id": None
        }
        self.departments = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology"
        ]
        self.teacher_list = [user for user in fakeDB["users"] if user["role"] == "teacher"]
        self.course_list = fakeDB["courses"]
        self.components = fakeDB["components"]
        self.component_id_counter = component_id_counter
        self.results = []
        
    def generate(self):
        for dept in self.departments:
            courses = [course for course in self.course_list if course["course_code"][0] == dept[0]]
            for course in courses:
                for _ in range(3):
                    self.components.append({
                        **self.component_default,
                        "uid": self.teacher_list[0]["uid"],
                        "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
                        "title": f"{dept} 課程討論 id = {self.component_id_counter}",
                        "content": f"{dept} 課程討論 id = {self.component_id_counter}"
                    })
                    self.results.append({
                        **self.default,
                        "id": self.component_id_counter,
                        "course_id": course["id"]
                    })
                    self.component_id_counter += 1

        return self.results, self.component_id_counter
