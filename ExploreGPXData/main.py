import gpxpy
import gpxpy.gpx
from math import radians, cos, sin, asin, sqrt


def readGPX(input_file):

    gpx_file = open(input_file, 'r')

    gpx = gpxpy.parse(gpx_file)

    data = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                latitude = point.latitude
                longitude = point.longitude
                elevation = point.elevation

                # ... print('Point at ({0},{1}) -> {2}'.format(latitude, longitude, elevation))

                data.append((latitude, longitude, elevation))

    max_points = len(data)

    print(data[1][0], data[1][1], data[0][0], data[0][1])

    for idx in range(1, max_points):

        lat1 = radians(data[idx-1][0])
        lat2 = radians(data[idx][0])
        lon1 = radians(data[idx-1][1])
        lon2 = radians(data[idx][1])

        d = distance(lat1, lat2, lon1, lon2)
        if d > 0.001:
            print(d, "KM")


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


if __name__ == '__main__':

    file = 'data/13.gpx'
    readGPX(file)
