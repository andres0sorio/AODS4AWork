from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
import json


class CarroYaScraper:
    """

    """
    def __init__(self):
        self.carroya_url = 'https://www.carroya.com/marcas-carros/'
        self.carroya_motos_url = 'https://www.carroya.com/marcas-motos/'
        self.results = []
        self.outfile = 'output/carroya_colombia_cars.html'
        self.outfile_motos = 'output/carroya_colombia_motos.html'

    def scrape(self):

        print(self.carroya_url)
        r = urllib.request.urlopen(self.carroya_url)
        site_content = r.read().decode('utf-8')

        # Saving scraped HTML to .html file (for later processing)
        with open(self.outfile, 'w') as f_out:
            f_out.write(site_content)

        print(self.carroya_motos_url)
        r = urllib.request.urlopen(self.carroya_motos_url)
        site_content = r.read().decode('utf-8')

        # Saving scraped HTML to .html file (for later processing)
        with open(self.outfile_motos, 'w') as f_out:
            f_out.write(site_content)

    def process(self):

        with open(self.outfile) as f_in:
            soup = BeautifulSoup(f_in, 'html.parser')
            all_links = soup.find_all('a', href=True)
            for a in all_links:
                href = a["href"]
                if "carros" in href:
                    brand_model = []
                    data = href.split('/')
                    data = list(filter(lambda x: x != "", data))
                    print(data)
                    if len(data) > 2:
                        brand_model.append(data[1])
                        brand_model.append(data[2])
                        self.results.append(brand_model)

        self.export_to_CSV("output/carros_colombia.csv")
        self.export_to_JSON("output/carros_colombia.json")

    def process_motos(self):

        with open(self.outfile_motos) as f_in:
            soup = BeautifulSoup(f_in, 'html.parser')
            all_links = soup.find_all('a', href=True)
            for a in all_links:
                href = a["href"]
                if "motos" in href:
                    brand_model = []
                    data = href.split('/')
                    data = list(filter(lambda x: x != "", data))
                    print(data)
                    if len(data) == 3 and data[0] == "motos":
                        brand_model.append(data[1])
                        brand_model.append(data[2])
                        self.results.append(brand_model)

        self.export_to_CSV("output/motos_colombia.csv")
        self.export_to_JSON("output/motos_colombia.json")

    def export_to_CSV(self, outfile_name):
        """

        """

        output_file = open(outfile_name, 'w', newline='')

        with output_file:
            writer = csv.writer(output_file, delimiter=';')
            writer.writerow(["Marca", "Modelo"])
            writer.writerows(self.results)

    def export_to_JSON(self, outfile_name):

        vehicles = {}

        for info in self.results:
            brand = info[0]
            vehicles[brand] = []

        for info in self.results:
            brand = info[0]
            models = info[1]
            vehicles[brand].append(models)

        with open(outfile_name, 'w') as f_out:
            json.dump(vehicles, f_out)

