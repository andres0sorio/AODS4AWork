from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'D:\\Temp\\chromedriver_win32\\chromedriver.exe'

import dryscrape


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

    def scrape3(self, input_file):
        """
        web Scraping with selenium+chromedriver
        unfortunately the SIMIT webpage has scraping blocking using captchas - which makes more difficult the task
          and not worth the effort (at least for this exercise)
        :param input_file: file with licence plates
        :return: html files to process with BS4
        """

        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get("https://www.fcm.org.co/simit/#/estado-cuenta?numDocPlacaProp=HQY866")
        print(driver.page_source)
        driver.quit()

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

    def scrape4(self, input_file):

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
