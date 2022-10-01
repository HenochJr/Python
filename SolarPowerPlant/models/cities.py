from solar_data import solar_data_portugal, solar_data_spain
from time import sleep


def portugal_city():
    global city_data
    city: str = input('Choose city from list (Lisboa, Aveiro, Setúbal, Almada, Porto, Nazaré): ')
    if city.lower() == 'lisboa':
        city_data = solar_data_portugal.lisboa
    elif city.lower() == 'aveiro':
        city_data = solar_data_portugal.aveiro
    elif city.lower() == 'setúbal' or city.lower() == 'setubal':
        city_data = solar_data_portugal.setubal
    elif city.lower() == 'almada':
        city_data = solar_data_portugal.almada
    elif city.lower() == 'porto':
        city_data = solar_data_portugal.porto
    elif city.lower() == 'nazaré' or city.lower() == 'nazare':
        city_data = solar_data_portugal.nazare
    else:
        print('Invalid city. Try again!')
        sleep(1)
        portugal_city()
    return city_data


def spain_city():
    global city_data
    city: str = input('Choose city from list (Madrid, Barcelona, Valência, Alicante): ')
    if city.lower() == 'madrid':
        city_data = solar_data_spain.madrid
    elif city.lower() == 'barcelona':
        city_data = solar_data_spain.barcelona
    elif city.lower() == 'valência' or city.lower() == 'valencia':
        city_data = solar_data_spain.valencia
    elif city.lower() == 'alicante':
        city_data = solar_data_spain.alicante
    else:
        print('Invalid city. Try again!')
        sleep(1)
        spain_city()
    return city_data