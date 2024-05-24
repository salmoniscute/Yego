from datetime import datetime

class DiscussionTopic:
    def __init__(self, fakeDB, component_id_counter):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title": None,
            "content": None
        }
        self.default = {
            "id": None,
            "discussion_id": None
        }
        self.departments = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology"
        ]
        self.teacher_list = [user for user in fakeDB["users"] if user["role"] == "teacher"]
        self.course_list = fakeDB["courses"]
        self.discussion_list = fakeDB["discussions"]
        self.components = fakeDB["components"]
        self.component_id_counter = component_id_counter
        self.results = []
        
    def generate(self):
        for dept in self.departments:
            courses = [course for course in self.course_list if course["course_code"][0] == dept[0]]
            for course in courses:
                discussions = [discussion for discussion in self.discussion_list if discussion["course_id"] == course["id"]]
                for discussion in discussions:
                    for _ in range(3): 
                        self.components.append({
                            **self.component_default,
                            "uid": self.teacher_list[0]["uid"],
                            "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
                            "title": f"{dept} 討論主題 id = {self.component_id_counter}",
                            "content": f"{dept} 討論主題 id = {self.component_id_counter}"
                        })
                        self.results.append({
                            **self.default,
                            "id": self.component_id_counter,
                            "discussion_id": discussion["id"]
                        })
                        self.component_id_counter += 1

        return self.results, self.component_id_counter
