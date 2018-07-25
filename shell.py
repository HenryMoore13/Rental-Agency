from core import *
from disk import *
from datetime import datetime


def greeting():
    print('\nWelcome To Henry Fords Rental Agency!!!\n')
    name = input('What Is Your Name? ')


def employee(inventory):
    load_inventory
    print('')
    program = input('\nWhat Would You Like To View?? ')


def Customer(inventory):
    print('--------------------------------------------------------------')
    print('\n (Ford Truck)  (Chevy Impala)  (Thunderbird)')
    buy = input('\nWhat Vehicle Would You Like To Rent? ').upper().strip()
    if buy == 'FORD TRUCK':
        rent = input('\nHow Many Days Would You Like To Rent? ')
        print(
            '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
            format(inventory['price'], rent))
    if buy == 'CHEVY IMPALA':
        rent = input('\nHow Many Days Would You Like To Rent? ')
        print(
            '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
            format(inventory['price'], rent))
    if buy == 'THUNDERBIRD':
        rent = input('\nHow Many Days Would You Like To Rent? ')
        print(
            '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
            format(inventory['price'], rent))


def choice(inventory):

    duty = input('\nAre You An Employee Or Customer?? ')
    while not (duty == '1' or duty == '2' or duty == '3'):
        print('Invalid Choice... Please Retype Choice')
        print()
        duty = input('>>> ').upper().strip()

    if duty == '1':
        employee()
    if duty == '2':
        Customer(inventory)
    if duty == '3':
        print('Thank You Come Again!!')
        exit()


def main():
    inventory = load_inventory()
    greeting()
    print('--------------------------------------------------------------')
    print('\nEnter:   (1)Employee   (2)Customer   (3)Quit')
    choice(inventory)
    load_inventory()


if __name__ == '__main__':
    main()
