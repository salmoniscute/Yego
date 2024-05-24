from datetime import datetime

class DiscussionTopicReply:
    def __init__(self, fakeDB, component_id_counter):
        self.component_default = {
            "uid": None,
            "release_time": None,
            "title": None,
            "content": None
        }
        self.default = {
            "id": None,
            "root_id": None,
            "parent_id": None
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
        self.discussion_topic_list = fakeDB["discussion_topics"]
        self.components = fakeDB["components"]
        self.component_id_counter = component_id_counter
        self.results = []
        
    def generate(self):
        for dept in self.departments:
            courses = [course for course in self.course_list if course["course_code"][0] == dept[0]]
            for course in courses:
                discussions = [discussion for discussion in self.discussion_list if discussion["course_id"] == course["id"]]
                for discussion in discussions:
                    topics = [topic for topic in self.discussion_topic_list if topic["discussion_id"] == discussion["id"]]
                    for topic in topics:
                        for reply in range(5):
                            if reply % 5 == 0:
                                parent = self.component_id_counter
                            self.components.append({
                                **self.component_default,
                                "uid": self.teacher_list[0]["uid"],
                                "release_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
                                "title": f"{dept} 討論回覆 id = {self.component_id_counter}",
                                "content": f"{dept} 討論回覆 id = {self.component_id_counter}"
                            })
                            self.results.append({
                                **self.default,
                                "id": self.component_id_counter,
                                "root_id": topic["id"],
                                "parent_id": parent if reply % 5 != 0 else 0
                            })
                            self.component_id_counter += 1

        return self.results, self.component_id_counter
    