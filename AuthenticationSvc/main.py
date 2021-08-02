from src.AuthServices import AuthServices


if __name__ == '__main__':

    step = 1

    if step == 0:

        try:
            new_user = {"username": "developer@rout90labs.com", "password": "Qwerty123$", "role": "client"}
            auth = AuthServices()
            auth.addUser(new_user)
            print("step 0: new user added")
        except Exception as e:
            print("Problem adding new user")
            print(e)

    elif step == 1:

        auth = AuthServices()
        data = {"username": "developer@rout90labs.com", "password": "Qwerty123$"}
        token = auth.authenticateJWT(data)
        print(token)

