from math import radians, cos, sin, asin, sqrt
import csv


def distance(lat1, lat2, lon1, lon2):
    """
    :param lat1: gps latitud point 1
    :param lat2: gps latitud point 2
    :param lon1: gps longitud point 1
    :param lon2: gps longitud point 2
    :return: distance in KM

    Credit to:
    https://www.geeksforgeeks.org/program-distance-two-points-earth/

    The great circle distance or the orthodromic distance is the shortest distance between two points
    on a sphere (or the surface of Earth). In order to use this method, we need to have the co-ordinates
    of point A and point B. The great circle method is chosen over other methods.

    """
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers.
    r = 6371

    # calculate the result
    return c*r


def exportToCSV(data, file_name, fields):

    output_file = open(file_name, 'w', newline='')

    with output_file:
        writer = csv.writer(output_file)
        writer.writerow(fields)
        writer.writerows(data)


def extractCoordinatesFromKML(input_file):

    f_out = open('data/output.xml', 'w')

    f_out.write("<?xml version=\"1.0\"?>\n")
    f_out.write("<MultiGeometry>\n")

    n_lines = 0

    with open(input_file) as f_in:
        line = f_in.readline()
        while line:
            line = f_in.readline()
            if "coordinates" in line:
                coordinates = line[:-1].strip(" ")
                f_out.write(coordinates + '\n')
                n_lines += 1

    f_out.write("</MultiGeometry>\n")
    f_out.close()

    print("NLINES: " + str(n_lines))


