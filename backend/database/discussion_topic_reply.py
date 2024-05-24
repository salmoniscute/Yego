from datetime import datetime

class DiscussionTopicReply:
    def __init__(self, fakeDB):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title": None,
            "content": None
        }
        self.default = {
            "id": None,
            "root_id": None,
            "parent_id": 0
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
                    topics = [topic for topic in self.DB["discussion_topics"] if topic["discussion_id"] == discussion["id"]]
                    for topic in topics:
                        for reply in range(5):
                            if reply % 5 == 0:
                                parent = component_id_counter
                            current_time = datetime.now()
                            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S") 
                            data = self.component_default.copy()
                            data["uid"] = self.teacher_list[0]["uid"]
                            data["release_time"] = formatted_time
                            data["title"] = f"{dept} 討論回覆 id = {component_id_counter}"
                            data["content"] = f"{dept} 討論回覆 id = {component_id_counter}"
                            components.append(data)
                            data = self.default.copy()
                            data["id"] = component_id_counter
                            data["root_id"] = topic["id"]
                            if reply % 5 != 0:
                                data["parent_id"] = parent
                            results.append(data)
                            component_id_counter += 1
        return results, component_id_counter