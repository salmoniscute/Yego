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
        self.results = []

    def random_uid(self, department):
        return department[0] + "".join(random.choices(string.digits, k=8))

    def random_password(self):
        characters = string.ascii_lowercase + string.digits
        return "".join(random.sample(characters, k=8))

    def random_introduction(self):
        return f"This is a random introduction: {str(random.randint(1, 1000))}"

    def generate(self):
        # Generate 15 students and 4 teachers/assistants for each department
        uid_counter = 0
        for dept in self.departments:
            for role in self.roles:
                count = 15 if role == "student" else 4
                for _ in range(count):
                    uid = self.random_uid(dept)
                    self.results.append({
                        **self.default,
                        "uid": uid,
                        "password": self.random_password(),
                        "name": role + str(uid_counter),
                        "role": role,
                        "email": f"{uid}@gs.ncku.edu.tw",
                        "department": dept,
                        "country": "Taiwan",
                        "introduction": self.random_introduction(),
                        "avatar": random.choice(["/assets/Yego.png", "/assets/Yegogo.png", "/assets/Dago.png"])
                    })
                    uid_counter += 1
        
        # Generate 1 admin
        self.results.append({
            **self.default,
            "uid": "admin",
            "password": "password",
            "name": "admin",
            "role": "admin",
            "email": "yego_admin@gs.ncku.edu.tw",
            "department": "admin",
            "country": "Taiwan",
            "introduction": None,
            "avatar": random.choice(["/assets/Yego.png", "/assets/Yegogo.png", "/assets/Dago.png"])
        })
        
        return self.results
