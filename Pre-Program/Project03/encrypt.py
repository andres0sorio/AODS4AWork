import json

n_val = 221
e_val = 5

"""
https://brilliant.org/wiki/rsa-encryption/
RSA is an encryption algorithm, used to securely transmit messages over the internet. 
It is based on the principle that it is easy to multiply large numbers, 
but factoring large numbers is very difficult. 
For example, it is easy to check that 31 and 37 multiply to 1147, 
but trying to find the factors of 1147 is a much longer process.
"""

def main():
    """
    main function call - no arguments
    :param name:
    :return:
    """

    print("Please enter text to encrypt: ")
    text = input()
    encrypted_text = encrypt(text)
    print(encrypted_text)


def encrypt(text):
    """
    Perform a simple encryption of a simple text - no especial characters allowed
    :param text: plain text without special characters
    :return: encrypted text
    """
    data = list(text.lower())
    encryption = []

    with open('table.json') as json_file:
        alphabet = json.load(json_file)

    for ch in data:
        translated = alphabet[ch]
        c = pow(translated, e_val) % n_val
        encryption.append(str(c))

    encrypted_text = "X".join(encryption)

    return encrypted_text


if __name__ == '__main__':
    main()

