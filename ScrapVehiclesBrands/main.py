from src.CarroYaScraper import CarroYaScraper


if __name__ == '__main__':

    step = 3
    scraper = CarroYaScraper()

    if step == 1:
        scraper.scrape()
    elif step == 2:
        scraper.process()
    elif step == 3:
        scraper.process_motos()
    else:
        print("All done!")

