import json

from database.user import User
from database.course import Course
from database.website_bulletin import WebsiteBulletin
from database.course_bulletin import CourseBulletin
from database.report import Report
from database.report_reply import ReportReply
from database.selected_course import SelectedCourse
from database.discussion import Discussion
from database.discussion_topic import DiscussionTopic
from database.discussion_topic_reply import DiscussionTopicReply
from database.file import File

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
    "discussion_topic_replies",
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
    
    def generate_selected_course(self):
        return SelectedCourse(self.output).generate()
    
    def generate_report(self):
        return Report(self.output, self.component_id_counter).generate()
    
    def generate_report_reply(self):
        return ReportReply(self.output, self.component_id_counter).generate()
    
    def generate_website_bulletin(self):
        return WebsiteBulletin(self.output, self.component_id_counter).generate()
    
    def generate_course_bulletin(self):
        return CourseBulletin(self.output, self.component_id_counter).generate()
    
    def generate_discussion(self):
        return Discussion(self.output, self.component_id_counter).generate()

    def generate_discussion_topic(self):
        return DiscussionTopic(self.output, self.component_id_counter).generate()

    def generate_discussion_topic_reply(self):
        return DiscussionTopicReply(self.output, self.component_id_counter).generate()
    
    def generate_file(self):
        return File(self.output).generate()

    def generate(self):
        self.output["users"] = self.generate_user()
        self.output["courses"] = self.generate_course()
        self.output["reports"], self.component_id_counter = self.generate_report()
        self.output["report_replies"], self.component_id_counter = self.generate_report_reply()
        self.output["website_bulletins"], self.component_id_counter = self.generate_website_bulletin()
        self.output["course_bulletins"], self.component_id_counter = self.generate_course_bulletin()
        self.output["selected_courses"] = self.generate_selected_course()
        self.output["discussions"], self.component_id_counter = self.generate_discussion()
        self.output["discussion_topics"], self.component_id_counter = self.generate_discussion_topic()
        self.output["discussion_topic_replies"], self.component_id_counter = self.generate_discussion_topic_reply()
        self.output["files"] = self.generate_file()
        
        with open("./database/fake_db.json", mode="w", encoding="utf-8") as file:
            json.dump(self.output, file, ensure_ascii=False, indent=4)
