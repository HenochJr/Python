from models.cities import portugal_city, spain_city
from time import sleep


def customer_location():
    global location_data
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
    print("Inform customer's location: ")
    country: str = input('Choose country from list (Portugal, Spain, Brazil, ...): ')
    if country.lower() == 'portugal':
        location_data = portugal_city()
    elif country.lower() == 'spain':
        location_data = spain_city()
    elif country.lower() == 'brazil':
        print("Brazil's solar data not available. Try again!")
        sleep(1)
        customer_location()
    else:
        print('Invalid country. Try again!')
        sleep(1)
        customer_location()
    return location_data


