from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv


class CarroYaScraper:
    """

    """
    def __init__(self):
        self.carroya_url = 'https://www.carroya.com/marcas-carros/'
        self.results = []
        self.outfile = 'output/carroya_colombia_cars.html'

    def scrape(self):

        print(self.carroya_url)
        r = urllib.request.urlopen(self.carroya_url)
        site_content = r.read().decode('utf-8')

        # Saving scraped HTML to .html file (for later processing)
        with open(self.outfile, 'w') as f_out:
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

        self.export_to_CSV()

    def export_to_CSV(self):
        """

        """

        output_file = open("output/carros_colombia.csv", 'w', newline='')

        with output_file:
            writer = csv.writer(output_file, delimiter=';')
            writer.writerow(["Marca", "Modelo"])
            writer.writerows(self.results)
