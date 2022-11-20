from Database import CDatabase


def load_users():
    db = CDatabase()
    return db.get_data()
