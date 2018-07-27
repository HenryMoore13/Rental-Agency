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
    buy = input('\nWhat Vehicle Would You Like To Rent? ').upper().strip()
    price = get_vehicleprice(buy)
    while not (buy == 'FORD TRUCK' or buy == 'CHEVY IMPALA'
               or buy == 'THUNDERBIRD'):
        print('Invalid Choice... Please Retype Choice')
        print()
        buy = input('>>> ').upper().strip()
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
    return (buy)
    return (rent)
    total = (price * rent)
    return (total)


def write_to_history(buy, rent, total):
    time = datetime.now()
    text = '\n{},{},{},{}'.format(buy, rent, time, total)
    with open('history.txt', 'a') as file:
        file.write(text)


def choice(inventory):

    duty = input('\nAre You An Employee Or Customer?? ')
    while not (duty == '1' or duty == '2' or duty == '3'):
        print('Invalid Choice... Please Retype Choice')
        print()
        duty = input('>>> ').upper().strip()

    if duty == '1':
        employee()
    if duty == '2':
        customer()
    if duty == '3':
        print('Thank You Come Again!!')
        exit()


def main():
    inventory = load_inventory()
    greeting()
    print('--------------------------------------------------------------')
    print('\nEnter:   (1)Employee   (2)Customer   (3)Quit')
    choice(inventory)
    save_inventory(inventory)
    buy = customer
    rent = customer
    total = customer
    write_to_history(buy, rent, total)


if __name__ == '__main__':
    main()
