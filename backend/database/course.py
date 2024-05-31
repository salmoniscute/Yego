import random
import string


class Course:
    def __init__(self, fakeDB):
        self.default = {
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
        self.results = []
    
    def generate(self):
        count = 1
        for teacher in self.teacher_list:
            department = teacher["department"][0]
            self.results.append({
                **self.default,
                "id": count,
                "uid": teacher["uid"],
                "course_code": department + "".join(random.choices(string.digits, k=3)),
                "name": f"Introduction to {department}",
                "academic_year": random.choice([2021, 2022, 2023]),
                "semester": random.choice([1, 2]),
                "outline": f"This course is an introduction to {department}."
            })
            count += 1
        
        return self.results
