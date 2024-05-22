import json

from user import User
from course import Course
from website_bulletin import WebsiteBulletin
from report import Report
from report_reply import ReportReply

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
        self.output["components"] = []
        self.component_id_counter = 1
    
    def generate_user(self):
        return User().generate()

    def generate_course(self):
        return Course(self.output).generate()
    
    def generate_report(self):
        return Report(self.output).generate(self.output["components"], self.component_id_counter)
    
    def generate_report_reply(self):
        return ReportReply(self.output).generate(self.output["components"], self.component_id_counter)
    
    def generate_website_bulletin(self):
        return WebsiteBulletin().generate(self.output["components"], self.component_id_counter)

    def generate(self):
        self.output["users"] = self.generate_user()
        self.output["courses"] = self.generate_course()
        self.output["reports"], self.component_id_counter = self.generate_report()
        self.output["report_replies"], self.component_id_counter = self.generate_report_reply()
        self.output["website_bulletins"], self.component_id_counter = self.generate_website_bulletin()

        with open(fakeDB, mode="w", encoding="utf-8") as file:
            json.dump(self.output, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    FakeDB().generate()
