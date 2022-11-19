import api_endpoint.api_endpoint as api
import api_endpoint.Database as db

if __name__ == '__main__':
    database = db.CDatabase()  # initialize create the database
    api.main()
