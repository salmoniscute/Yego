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
        self.teacher_list = [user for user in fakeDB["users"] if user["role"] == "teacher"]
    
    def generate(self):
        results = []
        count = 1
        for teacher in self.teacher_list:
            department = teacher["department"][0]

            course = self.default.copy()
            course["id"] = count
            course["uid"] = teacher["uid"]
            course["course_code"] = teacher["department"][0]+"".join(random.choices(string.digits, k=3))
            course["name"] = f"Introduction to {department}"
            course["academic_year"] = random.choice([2021, 2022, 2023])
            course["semester"] = random.choice([1, 2])
            course["outline"] = f"This course is an introduction to {department}."
            results.append(course)
            count += 1
        
        return results
