import hashlib
import os
import binascii


def create_hash(password):
    """
    https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
    :param password: plain password to be stored
    :return: salt and key to be stored in the db
    """

    salt = os.urandom(32)  # Remember this

    key = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),
        salt,
        100000
    )

    return salt.hex(), key.hex()


def hash_password(salt, password):
    """
    https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
    Modified by: Andres Osorio
    :param salt:
    :param password:
    :return:
    """
    salt_bin = binascii.unhexlify(salt)

    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt_bin,
        100000
    )

    return key.hex()

