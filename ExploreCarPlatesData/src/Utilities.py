import csv
import re

alpha_mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
inv_alpha_mapping = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}


def get_mintransport_data(input_file, logging):
    """

    :param input_file:
    :param logging:
    :return:
    """

    data = []

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                record = {"plate_range_min": row[0],
                          "plate_range_max": row[1],
                          "province": row[2],
                          "town": row[3],
                          "service": row[4]}
                data.append(record)

        return data

    except IOError as error:
        logging.info(error)
        return data


def encode_plate(plate):

    plate_pattern = re.compile(r'[a-z]{3}[0-9]{3}')

    plate = plate.lower()

    encoded_plate = 0

    if plate_pattern.search(plate):
        code = alpha_mapping[plate[0]]*10000 + alpha_mapping[plate[1]]*100 + alpha_mapping[plate[2]]*1
        series = int(plate[3:])
        encoded_plate = code*1000 + series

    return encoded_plate


def decode_plate(encoded_plate):

    series = str(encoded_plate)[-3:]

    pos_factor = {1: 10000, 2: 100, 3: 1}

    value = int(encoded_plate/1000)

    plate = ""
    factor = pos_factor[1]
    code = int(value/factor)
    plate += inv_alpha_mapping[code]

    step2_value = value - (factor*code)
    factor = pos_factor[2]
    code = int(step2_value/factor)
    plate += inv_alpha_mapping[code]

    step3_value = step2_value - (factor*code)
    factor = pos_factor[3]
    code = int(step3_value/factor)
    plate += inv_alpha_mapping[code]

    plate += series
    plate = plate.upper()

    return plate


def exportToCSV(data, file_name, fields):
    """

    :param data:
    :param file_name:
    :param fields:
    :return:
    """

    output_file = open(file_name, 'w', newline='', encoding='utf-8')

    with output_file:
        writer = csv.writer(output_file, delimiter=';')
        writer.writerow(fields)
        writer.writerows(data)
