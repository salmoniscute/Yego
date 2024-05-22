import json

from database.user import User
from database.course import Course
from database.selected_course import SelectedCourse

tables = [
    "users",
    "courses",
    "groups",
    "selected_courses",
    "components",
    "website_bulletins",
    "course_bulletins",
    "reports",
    "discussions",
    "discussion_topics",
    "subscriptions",
    "notifications"
]

class GenFakeDB:
    def __init__(self):
        self.output = {table: [] for table in tables}
    
    def generate_user(self):
        return User().generate()

    def generate_course(self):
        return Course(self.output).generate()
    
    def generate_selected_course(self):
        return SelectedCourse(self.output).generate()

    def generate(self):
        self.output["users"] = self.generate_user()
        self.output["courses"] = self.generate_course()
        self.output["selected_courses"] = self.generate_selected_course()

        with open("./database/fake_db.json", mode="w", encoding="utf-8") as file:
            json.dump(self.output, file, indent=4)
