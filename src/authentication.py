import os
from datetime import datetime, timedelta
from typing import Union

import cryptography.exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from jose import jwt


class Authentication:
    """
    Class which is used for authenticating of the users.
    IMPORTANT: OAuth2 functionalit, currently not in use (only future proofing).
    """

    # Secret key used for signing of the tokens
    _SECRET_KEY = "99f53be35765f14d7036067ee151aef6" \
                  "cf51d27844711d6c386a552c9ddfd57b"
    # Hash algorithm used during token creation
    _ALGORITHM = "HS256"
    # Expiration of token
    _ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # Error codes
    ERR_USR_NOT_FOUND = 1
    ERR_PWD_INVALID = 2
    ERR_USR_ALREADY_EXISTS = 3

    def __init__(self):
        self.fake_user_db = {}

    def create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None):
        """
        Creates the access token with the specified expiration.
        :param data: Data to encode into token
        :param expires_delta: Expiration time of the token
        :return: JWT encoded token
        """
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
        """
        Decodes the JWT encoded token into data.
        :param token: Token to decode
        :return: Decoded data from the token
        """
        return jwt.decode(token, self._SECRET_KEY, algorithms=[self._ALGORITHM])

    def get_user(self, username: str):
        """
        Gets the info about the specified user from the database of users.
        :param username: Username to find in the database.
        :return: Information about the user.
        """
        if username not in self.fake_user_db.keys():
            return self.ERR_USR_NOT_FOUND, {}
        return 0, self.fake_user_db[username]

    def validate_user(self, username: str, pwd: str) -> int:
        """
        Validates user credential against the database.
        :param username: Username of the user
        :param pwd: Password to check the user against
        :return: Error code
        """
        if username not in self.fake_user_db.keys():
            return self.ERR_USR_NOT_FOUND
        user_data = self.fake_user_db[username]
        pwd_hash = user_data["pwd_hash"]
        pwd_salt = user_data["pwd_salt"]
        err_code = self._verify_password(pwd, pwd_hash, pwd_salt)
        return err_code

    def _get_free_user_id(self):
        """
        Returns the next free id to use for the user
        :return: Next free ID for the new user
        """
        ids = [a["id"] for a in self.fake_user_db.values()]
        if len(ids) == 0:
            return 0
        return max(ids) + 1

    def add_user(self, username: str, pwd: str) -> int:
        """
        Adds the new user into the database.
        :param username: Username of the user
        :param pwd: Password of the user
        :return: Error code
        """
        if username in self.fake_user_db.keys():
            return self.ERR_USR_ALREADY_EXISTS
        salt_hex, pwd_hex = self._hash_password(pwd)
        self.fake_user_db[username] = {"pwd_salt": salt_hex, "pwd_hash": pwd_hex, "id": self._get_free_user_id()}
        return 0

    def rm_user(self, username: str) -> int:
        """
        Removes the specified user from the database.
        :param username: Username of the user to remove from the database.
        :return: Error code.
        """
        if username not in self.fake_user_db.keys():
            return self.ERR_USR_NOT_FOUND
        self.fake_user_db.pop(username)
        return 0

    @staticmethod
    def _hash_password(pwd: str):
        """
        Generates the salt and hashes the password using PBKDF2
        :param pwd: Password to hash
        :return: Tuple (salt hex, password hash hex)
        """
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
        """
        Verifies the password with the password hash.
        :param pwd: Password entered by user to check
        :param pwd_hash_hex: Saved password hash to check
        :param salt_hex: Saved salt to use
        :return: Error code (0 for success)
        """
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
