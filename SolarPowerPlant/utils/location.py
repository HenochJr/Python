from solar_data import solar_data_portugal
from time import sleep


def customer_location():
    global location_data
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
    print("Inform customer's location: ")
    country: str = input('Choose country from list (Portugal, ...): ')
    if country == 'Portugal':
        city: str = input('Choose city from list (Lisboa, Aveiro, Setúbal, Almada, Porto, Nazaré): ')
        if city == 'Lisboa':
            location_data = solar_data_portugal.lisboa
        elif city == 'Aveiro':
            location_data = solar_data_portugal.aveiro
        elif city == 'Setúbal':
            location_data = solar_data_portugal.setubal
        elif city == 'Almada':
            location_data = solar_data_portugal.almada
        elif city == 'Porto':
            location_data = solar_data_portugal.porto
        elif city == 'Nazaré':
            location_data = solar_data_portugal.nazare
        else:
            print('Invalid city. Try again!')
            sleep(1)
            customer_location()
    else:
        print('Invalid country. Try again!')
        sleep(1)
        customer_location()
    return location_data