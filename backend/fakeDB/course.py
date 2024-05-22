import random
import string


class Course:
    def __init__(self, fakeDB):
        self.default = {
            "id": None,
            "uid": None,
            "course_code": None,
            "academic_year": None,
            "semester": None,
            "name": None,
            "outline": None
        }
        self.departments = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology"
        ]
        self.teacher_list = [user["uid"] for user in fakeDB["users"] if user["role"] == "teacher"]


    def random_course_id(self, department):
        return department[0] + "".join(random.choices(string.digits, k=4))
    
    def generate(self):
        results = []

        for teacher in self.teacher_list:
            department = teacher[0]

            course = self.default.copy()
            course["id"] = self.random_course_id(department)
            course["uid"] = teacher
            course["course_code"] = course["id"]
            course["name"] = f"Introduction to {department}"
            course["academic_year"] = random.choice([2021, 2022, 2023])
            course["semester"] = random.choice([1, 2])
            course["outline"] = f"This course is an introduction to {department}."
            results.append(course)
        
        return results
