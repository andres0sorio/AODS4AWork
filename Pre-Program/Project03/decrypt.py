import json

p_val = 13
q_val = 17
e_val = 5


def main():
    """
    main function call - no arguments
    :param name:
    :return:
    """

    print("Please enter text to decrypt: ")
    text = input()
    decrypted_text = decrypt(text)
    print(decrypted_text)


def phi():
    """
    RSA - Phi(n) function
    :param:
    :return: phi(n)
    """
    return (p_val - 1)*(q_val - 1)


def transform(input_text):
    """
    Transform the input string into a useful list of integers
    :param input_text: encrypted text
    :return: list of integers
    """

    output = []
    data_str = input_text.split("X")
    for data in data_str:
        output.append(int(data))

    return output


def ApowBmodM(a, b, m):
    """
    https://www.geeksforgeeks.org/find-abm-large/
    We can write (a^b) % m as (a%m) * (a%m) * (a%m) * … (a%m), b times.
    :param a:
    :param b:
    :param m:
    :return:
    """
    # Find a%m
    ans = a % m
    mul = ans

    # now multiply ans by b-1 times and take
    # mod with m
    for i in range(1, b):
        ans = (ans*mul) % m

    return ans


def decrypt(text):
    """
    Perform a simple decryption of a simple text - no especial characters allowed
    :param text: plain text without special characters
    :return: decrypted text
    """
    data = transform(text)
    inv_alphabet = {}
    decryption = []

    n_val = p_val * q_val
    phi_n = phi()

    # Private key
    d = int(((2*phi_n) + 1)/e_val)

    with open('table.json') as json_file:
        alphabet = json.load(json_file)
        for key in alphabet:
            inv_alphabet[int(alphabet[key])] = key

    for ch in data:
        decrypted = ApowBmodM(ch, d, n_val)
        translated = inv_alphabet[decrypted]
        decryption.append(translated)

    decrypted_text = "".join(decryption)

    return decrypted_text


if __name__ == '__main__':
    main()

