from datetime import datetime


class Discussion:
    def __init__(self, fakeDB):
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
        self.DB = fakeDB
        self.teacher_list = [user for user in fakeDB["users"] if user["role"] == "teacher"]
        
    def generate(self, components, component_id_counter):
        results = []
        for dept in self.departments:
            courses = [course for course in self.DB["courses"] if course["course_code"][0] == dept[0]]
            courses = courses[:4]
            for course in courses:
                for _ in range(3):
                    current_time = datetime.now()
                    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S") 
                    data = self.component_default.copy()
                    data["uid"] = self.teacher_list[0]["uid"]
                    data["release_time"] = formatted_time
                    data["title"] = f"{dept} 課程討論 id = {component_id_counter}"
                    data["content"] = f"{dept} 課程討論 id = {component_id_counter}"
                    components.append(data)
                    data = self.default.copy()
                    data["id"] = component_id_counter
                    data["course_id"] = course["id"]
                    results.append(data)
                    component_id_counter += 1
        return results, component_id_counter