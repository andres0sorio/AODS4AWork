from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv


class SimitConsult:
    """

    """
    def __init__(self):
        self.simit_url = 'https://www.fcm.org.co/simit/#/estado-cuenta?numDocPlacaProp='
        self.results = []

    def scrape(self, input_file):

        with open(input_file, 'r', encoding='utf-8') as f_in:
            reader = csv.reader(f_in, delimiter=';')
            next(reader, None)

            for row in reader:
                plate = row[0]
                outfile = 'results/plate_' + plate + ".html"
                site_url = self.simit_url + plate
                print(site_url)
                r = urllib.request.urlopen(site_url)
                site_content = r.read().decode('utf-8')

                # Saving scraped HTML to .html file (for later processing)
                with open(outfile, 'w') as f_out:
                    f_out.write(site_content)

                self.results.append(outfile)

    def process(self):

        for file_name in self.results:

            with open(file_name) as f_in:
                soup = BeautifulSoup(f_in, 'html.parser')
                print(soup.prettify())
