from datetime import datetime


class SalesRepContact:
    def __init__(self):
        self.users_to_contact = []

    def save_user_for_call(self, username: str, phone_num: str, email: str, zip: str):
        self.users_to_contact.append(
            {
                "username": username,
                "phone": phone_num,
                "email": email,
                "zip": zip,
                "timestamp": datetime.now().strftime("%m/%d/%Y")
            }
        )

    def get_users_for_call(self):
        return self.users_to_contact
