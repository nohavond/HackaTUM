from datetime import datetime


class SalesRepContact:
    def __init__(self):
        self.users_to_contact = []

    def save_user_for_call(self, username: str, phone_num: str, email: str, zip: str):
        self.users_to_contact.append(
            {
                "username": username,
                "phone_num": phone_num,
                "email": email,
                "zip": zip,
                "created": datetime.now().timestamp()
            }
        )

    def get_users_for_call(self):
        return self.users_to_contact
