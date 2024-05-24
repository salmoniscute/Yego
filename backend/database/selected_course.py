import random


class SelectedCourse:
    def __init__(self, fakeDB):
        self.default = {
            "uid": None,
            "course_id": None,
            "group_id": None
        }

        self.department_dict = {
            "M": "Mathematics",
            "P": "Physics",
            "C": "Chemistry",
            "B": "Biology"
        }
        self.student_list = [user for user in fakeDB["users"] if user["role"] == "student"]
        self.teacher_list = [user for user in fakeDB["users"] if user["role"] == "teacher"]
        self.assistant_list = [user for user in fakeDB["users"] if user["role"] == "assistant"]
        self.course_list = [course for course in fakeDB["courses"]]
        self.results = []

    def generate(self):
        # 22 users (20 student + 1 teacher + 1 assistant) in 1 course
        for course in self.course_list:
            department = self.department_dict[course["course_code"][0]]

            # Add 20 students
            student_same_department = random.sample([student for student in self.student_list if student["department"] == department], 10)
            student_other_department = random.sample([student for student in self.student_list if student["department"] != department], 10)
            for student in student_same_department + student_other_department:
                self.results.append({
                    **self.default,
                    "uid": student["uid"],
                    "course_id": course["id"],
                    "group_id": None
                })

            # Add 1 teacher
            self.results.append({
                **self.default,
                "uid": random.choice([teacher for teacher in self.teacher_list if teacher["department"] == department])["uid"],
                "course_id": course["id"],
                "group_id": None
            })

            # Add 1 assistant
            self.results.append({
                **self.default,
                "uid": random.choice([assistant for assistant in self.assistant_list if assistant["department"] == department])["uid"],
                "course_id": course["id"],
                "group_id": None
            })

        return self.results
