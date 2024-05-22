import json

from database.user import User
from database.course import Course
from database.website_bulletin import WebsiteBulletin
from database.report import Report
from database.report_reply import ReportReply
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
    def generate_selected_course(self):
        return SelectedCourse(self.output).generate()

    def generate(self):
        self.output["users"] = self.generate_user()
        self.output["courses"] = self.generate_course()
        self.output["reports"], self.component_id_counter = self.generate_report()
        self.output["report_replies"], self.component_id_counter = self.generate_report_reply()
        self.output["website_bulletins"], self.component_id_counter = self.generate_website_bulletin()
        self.output["selected_courses"] = self.generate_selected_course()

        with open("./database/fake_db.json", mode="w", encoding="utf-8") as file:
            json.dump(self.output, file, ensure_ascii=False, indent=4)

