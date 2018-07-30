from core import *
from disk import *
from datetime import datetime


def greeting():
    print('\nWelcome To Henry Fords Rental Agency!!!\n')
    name = input('What Is Your Name? ')


def employee():
    inventory = load_inventory()
    print('(Inventory)   (Revenue)   (History)')
    program = input('\nWhat Would You Like To View?? ').upper().strip()
    while not (program == 'INVENTORY' or program == 'REVENUE'
               or program == 'HISTORY'):
        print('Invalid Choice... Please Retype Choice')
        print()
        program = input('>>> ').upper().strip()
    if program == 'INVENTORY':
        print()
        file = open('inventory.txt', 'r')
        contents = file.read()
        print(contents)
        file.close()
    if program == 'HISTORY':
        file = open('history.txt', 'r')
        contents = file.read()
        print(contents)
        file.close()


def customer():

    print('--------------------------------------------------------------')
    print('\n (Ford Truck)  (Chevy Impala)  (Thunderbird)')

    while True:
        price = get_vehicleprice()
        buy = input('\nWhat Vehicle Would You Like To Rent? ').upper().strip()
        if buy == 'FORD TRUCK':
            rent = input('\nHow Many Days Would You Like To Rent? ')
            print(
                '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
                format(price, rent))
        elif buy == 'CHEVY IMPALA':
            rent = input('\nHow Many Days Would You Like To Rent? ')
            print(
                '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
                format(price, rent))
        elif buy == 'THUNDERBIRD':
            rent = input('\nHow Many Days Would You Like To Rent? ')
            print(
                '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
                format(price, rent))
        else:
            print('Invalid Choice... Please Retype Choice')
            print()
            buy = input('>>> ').upper().strip()

        return (buy)
        return (rent)
        total = (price * rent)
        return (total)


def get_total(price, rent):
    price = get_vehicleprice()
    return price * rent


def write_to_history(buy, rent, total):
    rent = int(rent)
    buy = customer
    time = datetime.now()
    text = '\n{},{},{},{}'.format(buy, rent, time, total)
    with open('history.txt', 'a') as file:
        file.write(text)


def choice():

    duty = input('\nAre You An Employee Or Customer?? ')
    while not (duty == '1' or duty == '2' or duty == '3'):
        print('Invalid Choice... Please Retype Choice')
        print()
        duty = input('>>> ').upper().strip()

    if duty == '1':
        employee()
        exit()
    elif duty == '2':
        customer()
    elif duty == '3':
        print('Thank You Come Again!!')
        exit()


def main():
    get_vehicleprice()
    greeting()
    print('--------------------------------------------------------------')
    print('\nEnter:   (1)Employee   (2)Customer   (3)Quit')

    choice()
    buy = customer
    rent = int
    total = get_total
    )
    write_to_history(buy, rent, total)


if __name__ == '__main__':
    main()
