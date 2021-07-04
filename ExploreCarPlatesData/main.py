from src.SimitConsult import SimitConsult

if __name__ == '__main__':

    step = 1

    consult = SimitConsult()
    consult.scrape('data/placas.csv')
    consult.process()






