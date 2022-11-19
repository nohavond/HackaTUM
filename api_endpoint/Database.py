import sqlite3
from os.path import exists

import pandas as pd


class CDatabase:
    def __init__(self):
        self.name = 'users.db'
        self.id = 1
        if not exists(self.name):
            self.conn = sqlite3.connect(self.name)
            # adding table for the users
            self.conn.execute('''CREATE TABLE USER
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                         USERNAME TEXT          NOT NULL,
                         PHONE TEXT             NOT NULL,
                         EMAIL TEXT             NOT NULL,
                         ZIP INT                NOT NULL,
                         TIMESTAMP DATE         NOT NULL );''')

            self.__upload_data()
            self.conn.close()

    def __upload_data(self):
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('santhon0', '657-817-1288', 'nsteers0@meetup.com', '49884-122', '4/5/2022')");
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('dstanistreet1', '612-623-8329', 'itweedle1@issuu.com', '68703-056', '2/23/2022')");
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('mmacane2', '184-439-5728', 'khillum2@ebay.com', '0781-2865', '8/23/2022')");
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('mteaze3', '585-383-4362', 'mgoodchild3@howstuffworks.com', '36800-125', '6/26/2022')");
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('bguidera4', '372-107-8795', 'friglar4@walmart.com', '58232-0635', '1/16/2022')");
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('ihatfull5', '345-579-5158', 'rcheetham5@canalblog.com', '57520-0205', '6/21/2022')",);
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ( 'eoliva6', '234-991-6723', 'cpevie6@simplemachines.org', '55316-047', '11/17/2022')",);
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('cpessel7', '336-524-7466', 'kyakuntzov7@rediff.com', '58181-3031', '6/16/2022')",);
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('wbeiderbecke8', '259-281-0194', 'manchor8@scribd.com', '67938-2004', '10/1/2022')",);
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values ('crosenhaus9', '679-570-2066', 'areading9@ameblo.jp', '51329-2001', '4/4/2022')");
        print('Data uploaded successfully.')

    def add_data(self, data):
        self.conn = sqlite3.connect(self.name)
        user_data = (data['username'], data['phone'], data['email'], data[zip], data['timestamp'])
        self.conn.execute("insert into USER (username, phone, email, zip, timestamp) values (?,?,?,?,?)", user_data);

