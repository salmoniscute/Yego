import json

from auth.passwd import get_password_hash
from models.user import User as UserModel
from models.course import Course as CourseModel
from models.selected_course import SelectedCourse as SelectedCourseModel
from models.bulletin import CourseBulletin as CourseBulletinModel, WebsiteBulletin as WebsiteBulletinModel
from models.file import File as FileModel
from models.subscription import Subscription as SubscriptionModel
from models.notification import Notification as NotificationModel

model = {
    "users": UserModel,
    "courses": CourseModel,
    "selected_courses": SelectedCourseModel,
    "course_bulletins": CourseBulletinModel,
    "website_bulletins": WebsiteBulletinModel,
    "files": FileModel,
    "subscriptions": SubscriptionModel,
    "notifications": NotificationModel
}


class FakeDB:
    def __init__(self):
        with open("./database/fake_db.json") as file:
            self.data = json.load(file)

    async def create_entity_list(self, db_session):
        for table, entity_list in self.data.items():
            for entity in entity_list:
                if entity.get("password"):
                    entity["password"] = get_password_hash(entity["password"])
                
                row = model[table](**entity)
                db_session.add(row)
                