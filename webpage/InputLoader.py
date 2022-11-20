from Database import CDatabase


def load_users():
    db = CDatabase(r"C:\Users\Martin\Desktop\TUM\HackaTUM\db_data\users.db")
    return db.get_data()
