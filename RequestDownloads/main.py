import csv
import requests


def download(name):
    with open(name, 'r', encoding='utf-8') as f:

        reader = csv.reader(f)
        id = 1

        for row in reader:
            open_link= row[3]
            print(open_link)
            r = requests.get(open_link, allow_redirects=True)
            output_file = "./proyectos/Proyecto_" + str(id) + ".pdf"
            open(output_file, 'wb').write(r.content)
            id = id+1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file="Listado-proyectos.csv"
    download(input_file)
    print('Descargando')
