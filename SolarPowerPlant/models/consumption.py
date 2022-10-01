from time import sleep
from statistics import fmean

months: float = []
avg_cons: float = 0


def customer_cons():
    global avg_cons, months
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
    print("Inform customer's energy consumption: ")
    option: int = int(input('Inform month by month consumption (1) or annual average consumption (2) option: '))
    if option == 1:
        for month in year:
            months.append(float(input(f'Inform consumption for {month} (kWh): ')))
            avg_cons = fmean(months)
    elif option == 2:
        avg_cons = float(input('Inform annual average consumption (kWh): '))
    else:
        print('Invalid option. Try again!')
        sleep(1)
        customer_cons()
    return avg_cons, months