import xml.etree.ElementTree as ET
from Extras.Utilities import *
from CoordinateMatcher import CoordinateMatcher


def parseXML(input_file):
    """
    This function parses a clean XML file and runs the analysis for producing an equivalence table
       between KM on road coordinates (latitude, longitude)
    :param input_file: clean XML file
    :return: nothing
    """

    tree = ET.parse(input_file)
    root = tree.getroot()

    points_str = []
    coordinates_data = []
    equivalence_data = []

    for coordinate_elem in root.iter('coordinates'):
        coordinate_text = coordinate_elem.text.split(" ")
        str_list = list(filter(lambda x: x != '\n', coordinate_text))
        str_list = list(filter(None, str_list))
        str_list = list(map(lambda s: s.strip(), str_list))

        for coord in str_list:
            points_str.append(coord)

    for pts_str in points_str:
        coordinates = pts_str.split(",")
        longitude = float(coordinates[0])
        latitude = float(coordinates[1])
        elevation = float(coordinates[2])

        # ... print(latitude, ",", longitude)

        coordinates_data.append([latitude, longitude, elevation])

    max_points = len(coordinates_data)

    total_distance = 0.0

    p_starting_point = coordinates_data[0]
    p_end_point = coordinates_data[-1]

    print(p_starting_point, p_end_point)

    for idx in range(1, max_points):

        lat1 = coordinates_data[idx-1][0]
        lat2 = coordinates_data[idx][0]
        lon1 = coordinates_data[idx-1][1]
        lon2 = coordinates_data[idx][1]
        ele1 = coordinates_data[idx-1][2]

        d = distance(lat1, lat2, lon1, lon2)

        if 0.010 < d < 0.015:
            total_distance += d
            print(lat1, lon1, ele1, total_distance, d)
            equivalence_data.append([lat1, lon1, ele1, total_distance, d])

    print(total_distance)

    exportToCSV(equivalence_data, 'data/equivalence_table.csv', ['latitude', 'longitude', 'elevation', 'cumulative', 'd'])


if __name__ == '__main__':

    step = 2

    # Step 0. Clean KML file from all unnecessary data
    # Step 1. Generate the equivalence table based on KML points
    # Step 2. MATCH coordinate to ABS KM

    if step == 1:
        file_01 = "data/Puntos_c10m_viaJuncal_Flandes_CondatosZ_V3_CLEAN.xml"
        parseXML(file_01)

    elif step == 2:

        matcher = CoordinateMatcher('data/equivalence_table.csv')

        # TODO: clean this section: this must be done in a more systematic way
        #  matcher.match_input('data/Siniestros autovia_KMS_Original.csv')
        #  matcher.match_input('data/highest_accidents_by_km.csv')

        # matcher.match_input('data/Informe_Unificado_VARADOS_Rev1_ABSISAS.csv')
        matcher.match_input('data/Compilado DS4A_Rev3_Absisas.csv')

        matcher.export()

    elif step == 0:

        extractCoordinatesFromKML('data/Puntos_c10m_viaJuncal_Flandes_CondatosZ_V3.kml')

    else:
        print("No more options available")
