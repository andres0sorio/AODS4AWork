from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
import dryscrape
from selenium import webdriver
import time


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

    def scrape2(self, input_file):

        dryscrape.start_xvfb()
        
        with open(input_file, 'r', encoding="utf-8") as f_in:
            reader = csv.reader(f_in, delimiter=";")
            next(reader,None)

            for row in reader:
                plate = row[0]
                outfile = 'results/plate_' + plate + ".html"
                site_url = self.simit_url + plate

                session = dryscrape.Session(base_url=site_url)
                session.set_attribute('auto_load_images', False)
                session.visit("/")
                response = session.body()
                print("Done with site: ", site_url)
                print(response)
                
                # Saving scraped HTML to .html file (for later processing)
                with open(outfile, 'w') as f_out:
                    f_out.write(response)
                
                self.results.append(outfile)
                

    def scrape3(self, input_file):

        driver = webdriver.Firefox()
        
        with open(input_file, 'r', encoding="utf-8") as f_in:
            reader = csv.reader(f_in, delimiter=";")
            next(reader,None)

            for row in reader:
                plate = row[0]
                outfile = 'results/plate_' + plate + ".html"
                site_url = self.simit_url + plate
                print(site_url)
                driver.get(site_url)
                
        
    def process(self):

        for file_name in self.results:

            with open(file_name) as f_in:
                soup = BeautifulSoup(f_in, 'html.parser')
                print(soup.prettify())
