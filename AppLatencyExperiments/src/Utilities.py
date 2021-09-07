import csv


def exportToCSV(data, file_name, fields):
    """
    :param data:
    :param file_name:
    :param fields:
    :return:
    """

    output_file = open(file_name, 'w', newline='')

    with output_file:
        writer = csv.writer(output_file, delimiter=';')
        writer.writerow(fields)
        writer.writerows(data)
