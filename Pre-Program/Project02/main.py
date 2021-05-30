import json
import re


def main():
    """
    Little script to perform a translation from plain english to lolspeak
    :return:
    """
    print("*---------------------------------------*")
    print("Please enter the file path to translate: ")
    input_file = input()

    try:
        translate(input_file)
    except FileNotFoundError:
        print("Please enter the correct file name (FileNotFoundError)")

    print("Translation to LOLSPEAK - Done")


def read_dictionary():

    with open('tranzlashun.json') as json_file:
        lolspeak_table = json.load(json_file)

    return lolspeak_table


def translate(input_filename):
    """
    Translate from plain english to lolspeak
    :param input_filename: file to process
    :return: nothing - creates new file with translated text
    """

    with open(input_filename) as input_file:

        output_filename= input_filename.split(".")[0] + "_lolcat.txt"
        output_file = open(output_filename, 'w')
        lolspeak_dict = read_dictionary()

        for line in input_file:

            data = line.split()
            translated_line = []
            for wd in data:
                wd_lower = wd.lower()
                wd_clean = re.sub(r'[^a-z]', '', wd_lower)

                try:
                    translation = "*" + lolspeak_dict[wd_clean] + "*"
                    translated_line.append(translation)
                except KeyError:
                    translated_line.append(wd_clean)

                translated_line.append(" ")

            translated_line.append('\n')
            output_file.writelines(translated_line)

    output_file.close()


if __name__ == '__main__':
    main()


