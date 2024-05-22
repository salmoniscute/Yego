import random
import string


class User:
    def __init__(self):
        self.default = {
            "uid": None,
            "password": None,
            "name": None,
            "role": None,
            "email": None,
            "department": None,
            "country": None,
            "introduction": None,
            "avatar": None
        }

        self.departments = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology"
        ]
        self.roles = [
            "student", 
            "teacher", 
            "assistant"
        ]

    def random_uid(self, department):
        return department[0] + "".join(random.choices(string.digits, k=8))

    def random_password(self):
        characters = string.ascii_lowercase + string.digits
        return "".join(random.sample(characters, k=8))

    def random_introduction(self):
        return f"This is a random introduction: {str(random.randint(1, 1000))}"

    def generate(self):
        results = []

        # Generate 15 students and 4 teachers/assistants for each department
        uid_counter = 0
        for dept in self.departments:
            for role in self.roles:
                count = 15 if role == "student" else 4
                for _ in range(count):
                    user = self.default.copy()
                    user["uid"] = self.random_uid(dept)
                    user["password"] = self.random_password()
                    user["name"] = role + str(uid_counter)
                    user["role"] = role
                    user["email"] = f"{user["uid"]}@gs.ncku.edu.tw"
                    user["department"] = dept
                    user["country"] = "Taiwan"
                    user["introduction"] = self.random_introduction()
                    user["avatar"] = "backend/upload/user/default/default.jpg"
                    
                    results.append(user)
                    uid_counter += 1
        
        # Generate 1 admin
        user = self.default.copy()
        user["uid"] = "admin"
        user["password"] = "password"
        user["name"] = "admin"
        user["role"] = "admin"
        user["email"] = "yego_admin@gs.ncku.edu.tw"
        user["department"] = "admin"
        user["introduction"] = None
        user["avatar"] = "backend/upload/user/default/default.png"
        results.append(user)

        return results
