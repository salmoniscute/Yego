import json

from user import User
from course import Course

fakeDB = "fake_db.json"
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

class FakeDB:
    def __init__(self):
        self.output = {table: [] for table in tables}
    
    def generate_user(self):
        return User().generate()

    def generate_course(self):
        return Course(self.output).generate()

    def generate(self):
        self.output["users"] = self.generate_user()
        self.output["courses"] = self.generate_course()

        with open(fakeDB, mode="w", encoding="utf-8") as file:
            json.dump(self.output, file, indent=4)


if __name__ == '__main__':
    FakeDB().generate()
