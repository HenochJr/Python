from models.customer import customer_reg
from models.location import customer_location
from models.consumption import customer_cons
from statistics import fmean
from time import sleep

print('====================================================')
print('=========== Solve Engineering & Services ===========')
print('========= Photovoltaic Power Plant Sizing ==========')
print('====================================================')


def main() -> None:
    sizing()


def sizing() -> None:
    customer: str = customer_reg()
    solar_data: float = customer_location()
    consumption: float = customer_cons()
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
    print("Inform technical data for sizing system:")
    capacity_factor = 0.9
    perc_power: float = float(input("Desired power generated by system (%): "))
    panel_power: float = float(input("Rated power of each photovoltaic panel (W): "))
    required_rated_power: float = ((perc_power / 100) * consumption[0]) / ((365 / 12) * fmean(solar_data))
    required_panels: float = round(((required_rated_power * 1000) / panel_power) / capacity_factor + 1)
    required_inverter: float = round(required_panels * panel_power / 1000)
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
    print(f'{customer[0]}, your photovoltaic system should be composed by: ')
    print(f'1 - {required_inverter:,.1f}kW inverter and')
    print(f'{required_panels:,.0f} - {panel_power}W photovoltaic solar panels with'
          f' a total of {panel_power * required_panels / 1000:,.2f}kWp installed power.')
    sleep(2)


if __name__ == '__main__':
    main()

if input('\nPress any key to exit') != '':
    exit(0)
