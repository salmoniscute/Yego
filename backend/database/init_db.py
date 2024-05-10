import json

from auth.passwd import get_password_hash
from models.user import User as UserModel
from models.course import Course as CourseModel
from models.selected_course import SelectedCourse as SelectedCourseModel
from models.component import Component as ComponentModel
from models.bulletin import CourseBulletin as CourseBulletinModel, WebsiteBulletin as WebsiteBulletinModel
from models.file import File as FileModel
from models.subscription import Subscription as SubscriptionModel
from models.notification import Notification as NotificationModel
from models.course_material import CourseMaterial as CourseMaterialModel, MaterialInfo as MaterialInfoModel, SubmittedAssignment as SubmittedAssignmentModel
from models.discussion import Discussion as DiscussionModel, DiscussionTopic as DiscussionTopicModel
from models.report import Report as ReportModel
from models.group import Group as GroupModel

model = {
    "users": UserModel,
    "courses": CourseModel,
    "selected_courses": SelectedCourseModel,
    "groups": GroupModel,
    "components": ComponentModel,
    "course_bulletins": CourseBulletinModel,
    "website_bulletins": WebsiteBulletinModel,
    "files": FileModel,
    "subscriptions": SubscriptionModel,
    "notifications": NotificationModel,
    "course_materials": CourseMaterialModel,
    "discussions": DiscussionModel,
    "discussion_topics": DiscussionTopicModel,
    "reports": ReportModel
}


class FakeDB:
    def __init__(self):
        with open("./database/fake_db.json", encoding="utf8") as file:
            self.data = json.load(file)

    async def create_entity_list(self, db_session):
        for table, entity_list in self.data.items():
            for entity in entity_list:
                if entity.get("password"):
                    entity["password"] = get_password_hash(entity["password"])
                
                row = model[table](**entity)
                db_session.add(row)
                