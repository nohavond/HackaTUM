import os
from datetime import datetime, timedelta
from typing import Union

import cryptography.exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from jose import jwt


class Authentication:
    _SECRET_KEY = "99f53be35765f14d7036067ee151aef6" \
                  "cf51d27844711d6c386a552c9ddfd57b"
    _ALGORITHM = "HS256"
    _ACCESS_TOKEN_EXPIRE_MINUTES = 30

    ERR_USR_NOT_FOUND = 1
    ERR_PWD_INVALID = 2
    ERR_USR_ALREADY_EXISTS = 3

    def __init__(self):
        self.fake_user_db = {}

    def create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._SECRET_KEY,
                                 algorithm=self._ALGORITHM)
        return encoded_jwt

    def decode_access_token(self, token: str):
        return jwt.decode(token, self._SECRET_KEY, algorithms=[self._ALGORITHM])

    def get_user(self, username: str):
        if username not in self.fake_user_db.keys():
            return self.ERR_USR_NOT_FOUND, {}
        return 0, self.fake_user_db[username]

    def validate_user(self, username: str, pwd: str) -> int:
        if username not in self.fake_user_db.keys():
            return self.ERR_USR_NOT_FOUND
        user_data = self.fake_user_db[username]
        pwd_hash = user_data["pwd_hash"]
        pwd_salt = user_data["pwd_salt"]
        err_code = self._verify_password(pwd, pwd_hash, pwd_salt)
        return err_code

    def _get_free_user_id(self):
        ids = [a["id"] for a in self.fake_user_db.values()]
        if len(ids) == 0:
            return 0
        return max(ids) + 1

    def add_user(self, username: str, pwd: str) -> int:
        if username in self.fake_user_db.keys():
            return self.ERR_USR_ALREADY_EXISTS
        salt_hex, pwd_hex = self._hash_password(pwd)
        self.fake_user_db[username] = {"pwd_salt": salt_hex, "pwd_hash": pwd_hex, "id": self._get_free_user_id()}
        return 0

    def rm_user(self, username: str) -> int:
        if username not in self.fake_user_db.keys():
            return self.ERR_USR_NOT_FOUND
        self.fake_user_db.pop(username)
        return 0

    @staticmethod
    def _hash_password(pwd: str):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        pwd_bytes = pwd.encode('utf-8')
        hashed = kdf.derive(pwd_bytes)
        return salt.hex(), hashed.hex()

    @staticmethod
    def _verify_password(pwd: str, pwd_hash_hex: str, salt_hex: str) -> int:
        salt = bytes.fromhex(salt_hex)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        pwd_bytes = pwd.encode('utf-8')
        try:
            kdf.verify(pwd_bytes, bytes.fromhex(pwd_hash_hex))
            return 0
        except cryptography.exceptions.InvalidKey:
            return Authentication.ERR_PWD_INVALID
