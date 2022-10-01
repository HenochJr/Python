from time import sleep

cust_data: str = []
year = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
        'december']


def customer_reg():
    print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
    print("Inform customer's personnel data: ")
    fields = ['name', 'address', 'email', 'phone']
    for data in fields:
        cust_data.append(str(input(f"Customer's {data}: ")))
    sleep(1)
    return cust_data