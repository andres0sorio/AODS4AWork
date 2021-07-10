from src.CarroYaScraper import CarroYaScraper


if __name__ == '__main__':

    step = 2
    scraper = CarroYaScraper()

    if step == 1:
        scraper.scrape()
    elif step == 2:
        scraper.process()
    else:
        print("All done!")

