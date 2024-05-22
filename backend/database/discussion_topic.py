from datetime import datetime

class DiscussionTopic:
    def __init__(self, fakeDB):
        self.component_default = {
            "uid": "F74102048",
            "release_time": "2024-04-10 16:10:05",
            "title": "討論主題一",
            "content": "這是第一個討論主題"
        }
        self.default = {
            "id": 1,
            "discussion_id": 1
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
                discussions = [discussion for discussion in self.DB["discussions"] if discussion["course_id"] == course["id"]]
                for discussion in discussions:
                    for _ in range(3):
                        current_time = datetime.now()
                        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S") 
                        data = self.component_default.copy()
                        data["uid"] = self.teacher_list[0]["uid"]
                        data["release_time"] = formatted_time
                        data["title"] = f"{dept} 討論主題 id = {component_id_counter}"
                        data["content"] = f"{dept} 討論主題 id = {component_id_counter}"
                        components.append(data)
                        data = self.default.copy()
                        data["id"] = component_id_counter
                        data["discussion_id"] = discussion["id"]
                        results.append(data)
                        component_id_counter += 1
        return results, component_id_counter