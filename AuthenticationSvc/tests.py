import unittest
import sqlite3
import jwt
from sqlite3 import Error
from src.AuthServices import AuthServices
from src.Utilities import *
from src.Configuration import Configuration


class MyTestCase(unittest.TestCase):

    def test_sqlite_connection(self):

        con = None

        try:
            con = sqlite3.connect('users.db')
            cur = con.cursor()
            print('SQLITE database version:')
            db_version = sqlite3.version
            print(sqlite3.version)
            con.close()
            self.assertEqual(db_version, "2.6.0")

        except Error as e:
            print(e)

        finally:
            if con:
                con.close()

    def test_sqlite_users(self):
        """

        :return:
        """

        con = sqlite3.connect('users.db')
        self.delete_test_table(con)
        cur = con.cursor()
        try:

            cur.execute('''CREATE TABLE user_tests
                   (username text, salt text, key text, role text)''')
            cur.execute("INSERT INTO user_tests VALUES ('developer@rout90labs.com', 'SALT', 'PEPPER', 'dev')")
            con.commit()
        except Error as e:
            print(e)

        con.close()

    def test_sqlite_added_users(self):
        """

        :return:
        """
        con = sqlite3.connect('users.db')
        cur = con.cursor()

        for row in cur.execute('SELECT * FROM user_tests ORDER BY username'):
            self.assertEqual(row[0], "developer@rout90labs.com")
            self.assertEqual(row[1], "SALT")
            self.assertEqual(row[2], "PEPPER")
            self.assertEqual(row[3], "dev")
            print(row)

    def delete_all_users(self, conn):
        """
        Delete all rows in the tasks table
        :param conn: Connection to the SQLite database
        :return:
        """
        sql = 'DELETE FROM user_tests'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    def delete_test_table(self, conn):
        """
        Delete all rows in the tasks table
        :param conn: Connection to the SQLite database
        :return:
        """
        sql = 'DROP TABLE user_tests'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    def test_add_user(self):
        """

        :return:
        """
        auth = AuthServices()
        data = {"username": "andres.osorio@outlook.com", "password": "Qwerty123$", "role": "admin"}
        auth.addUser(data)

        con = sqlite3.connect('users.db')
        cur = con.cursor()

        for row in cur.execute('SELECT * FROM users'):
            print(row)

    def test_hash_procedure(self):

        users = {}
        salt, key = hash_password("Qwerty123$")

        users["tester@user"] = {
            'salt': salt,
            'key': key
        }

        print(users)

    def test_authenticate(self):

        auth = AuthServices()
        data = {"username": "andres.osorio@outlook.com", "password": "Qwerty123$", "role": "admin"}
        auth.authenticate(data)

        wrong_data = {"username": "andres.osorioo@outlook.com", "password": "Qwerty123$", "role": "admin"}
        auth.authenticate(wrong_data)

        wrong_data = {"username": "andres.osorio@outlook.com", "password": "SOMETHING", "role": "admin"}
        auth.authenticate(wrong_data)

    def test_config(self):

        config = Configuration()
        secret_key = config.getSecretKey()
        print(secret_key)
        self.assertFalse(secret_key is 'NOSECRET')

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        Inspiration from:
        https://realpython.com/token-based-authentication-with-flask
        https://pyjwt.readthedocs.io/en/stable/
        :param auth_token:
        :return: integer|string
        """
        try:
            config = Configuration()
            payload = jwt.decode(auth_token, config.getSecretKey(), algorithms=["HS256"])
            return payload

        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'

        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def test_jwt(self):

        auth = AuthServices()
        data = {"username": "andres.osorio@outlook.com", "password": "Qwerty123$"}
        token = auth.authenticateJWT(data)
        payload = self.decode_auth_token(token)
        print(payload['sub'], payload['exp'])


if __name__ == '__main__':
    unittest.main()
