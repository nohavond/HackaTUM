import api.api_endpoint as api
import api.Database as db

if __name__ == '__main__':
    database = db.CDatabase()  # initialize create the database
    api.main()
