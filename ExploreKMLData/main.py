import xml.etree.ElementTree as ET
from Extras.Utilities import *
from CoordinateMatcher import CoordinateMatcher


def parseXML(input_file):

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

        print(latitude, ",", longitude)

        coordinates_data.append([latitude, longitude, elevation])

    max_points = len(coordinates_data)

    total_distance = 0.0

    p_juncal = coordinates_data[0]
    p_flandes = coordinates_data[-1]
    print(p_juncal, p_flandes)

    for idx in range(1, max_points):

        lat1 = coordinates_data[idx-1][0]
        lat2 = coordinates_data[idx][0]
        lon1 = coordinates_data[idx-1][1]
        lon2 = coordinates_data[idx][1]

        d = distance(lat1, lat2, lon1, lon2)

        if d > 0.050:
            total_distance += d
            print(lat1, lon1, total_distance, d)
            equivalence_data.append([lat1, lon1, total_distance, d])

    print(total_distance)

    # exportToCSV(coordinates_data, 'data/extracted_coordinates.csv')

    exportToCSV(equivalence_data, 'data/equivalence_table.csv', ['latitude', 'longitude', 'cumulative', 'd'])


if __name__ == '__main__':

    file_01 = 'data/Juncal-Flandes_IGAC.xml'
    file_02 = 'data/Puntos_c100m_viaJuncal_Flandes.kml'
    file_03 = "data/output.xml"

    #parseXML(file_03)
    # Google maps latitud y luego longitud
    # 2.8873968596085753, -75.3443901848703
    # 2.8726516219645015, -75.34078516405859
    d = distance(2.8873968596085753,2.8726516219645015, -75.3443901848703, -75.34078516405859)
    print("*", d)  # Resultado OK

    # MATCH coordinate to ABS KM

    matcher = CoordinateMatcher('data/equivalence_table.csv')

    matcher.match_input('data/Siniestros autovia_KMS_Original.csv')

    matcher.export()

