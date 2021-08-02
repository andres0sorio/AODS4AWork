import jwt
import datetime
import sqlite3
from sqlite3 import Error
from .Utilities import *
from .Configuration import *


class AuthServices:
    """
    Authentication services with JWT
    - Users are created and added to a local sqlite db (this is for practical reasons)
    Author: Andres Osorio
    Date: 01/08/2021
    """
    def __init__(self):
        self.config = Configuration()
        self.table = self.config.getUserTable()
        self.con = sqlite3.connect('users.db')
        try:
            cur = self.con.cursor()
            cur.execute("CREATE TABLE " + self.table + " (username text, salt text, key text, role text)")
        except Error as e:
            print(e)

    def authenticate(self, data):
        """

        :param data:
        :return:
        """
        username = data["username"]
        input_pwd = data["password"]

        try:
            result = self.getUserKey(username)
            salt = result[0]
            stored_key = result[1]
            key = hash_password(salt, input_pwd)

            assert key == stored_key

            return True

        except TypeError:
            print("Error from DB- user does not exist")
            return False

        except AssertionError:
            print("Password does not match - be careful")
            return False

    def authenticateJWT(self, data):
        """

        :param data:
        :return:
        """
        try:

            is_user_valid = self.authenticate(data)
            if is_user_valid:
                return self.getToken(data)

        except Exception as e:
            print(e)
            print("Cannot authenticate USER")
            return {}

    def getToken(self, data):
        """

        :param data:
        :return:
        """
        username = data["username"]

        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
                'iat': datetime.datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(payload, self.config.getSecretKey(), algorithm='HS256')

        except Exception as e:
            return e

    def getUserKey(self, username):

        try:
            cur = self.con.cursor()
            cmd = "select salt, key from " + self.table + " where username=\"" + username + "\""
            result = cur.execute(cmd).fetchone()
            return result

        except Exception as e:
            print(e)
            raise e

# ...
# ... The following section is a very user db interface that for practical reason is done here
# ...

    def addUser(self, data):
        """

        :param data:
        :return:
        """
        print(data)
        username = data["username"]
        password = data["password"]
        role = data["role"]

        salt, key = create_hash(password)

        cur = self.con.cursor()
        try:
            cmd = "INSERT INTO " + self.table + " VALUES ('" + username + "','" \
                  + salt + "','" \
                  + key + "','" \
                  + role + "')"
            print(cmd)
            cur.execute(cmd)
            self.con.commit()

        except Error as e:
            print(e)
