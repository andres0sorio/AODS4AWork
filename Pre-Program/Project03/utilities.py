import string
import json


def main():
    """
    Encryption function
    :param name:
    :return:
    """
    alpha = list(string.ascii_lowercase)
    table = {}

    for i in range(0,len(alpha)):
        table[alpha[i]] = i+1

    with open("table.json", "w") as fp:
        json.dump(table, fp)


if __name__ == '__main__':
    main()
