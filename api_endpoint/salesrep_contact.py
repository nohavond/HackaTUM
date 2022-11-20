from datetime import datetime
import Database as db


class SalesRepContact:
    def __init__(self, database: db.CDatabase):
        self.database = database

    def save_user_for_call(self, username: str, phone_num: str, email: str, zip: str):
        self.database.add_data({
            "username": username,
            "phone": phone_num,
            "email": email,
            "zip": zip,
            "timestamp": datetime.now().strftime("%m/%d/%Y")
        })

    def get_users_for_call(self):
        users = self.database.get_data()
        return users
