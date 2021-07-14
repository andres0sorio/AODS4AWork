from src.SimitConsult import SimitConsult
from src.PlateRegistration import PlateRegistrationPlace


if __name__ == '__main__':

    step = 2

    if step == 1:
        consult = SimitConsult()
        consult.scrape3('data/placas.csv')
        consult.process()

    elif step == 2:
        registration = PlateRegistrationPlace()
        print(registration.records[10])
        registration.prepare_bins()
        registration.match_information('data/licence_plates.csv')
        registration.export_information('results/licence_plates_info.csv')

    else:
        print("All done for now!")
