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


def get_option():
    print('--------------------------------------------------------------')
    print()
    print('      (Rent)           (Return)')
    option = input('\nWould your like to rent a Vehicle or return one?\n')
    if option == 'RENT':
        customer()
    elif option == 'RETURN':
        print('thanks for shopping with our Rental Agency Come again!!')


def customer():

    print('--------------------------------------------------------------')
    print('\n (Ford Truck)  (Chevy Impala)  (Thunderbird)')

    while True:

        buy = input('\nWhat Vehicle Would You Like To Rent? ').upper().strip()
        if buy == 'FORD TRUCK':
            rent = input('\nHow Many Days Would You Like To Rent? ')
            print(
                '\nThis Vehicle Will be $210 per day & you have {} days to return it!!'.
                format(rent))
        elif buy == 'CHEVY IMPALA':
            rent = input('\nHow Many Days Would You Like To Rent? ')
            print(
                '\nThis Vehicle Will be $120 per day & you have {} days to return it!!'.
                format(rent))
        elif buy == 'THUNDERBIRD':
            rent = input('\nHow Many Days Would You Like To Rent? ')
            print(
                '\nThis Vehicle Will be $150 per day & you have {} days to return it!!'.
                format(rent))
        else:
            print('Invalid Choice... Please Retype Choice!!')
            print()
            buy = input('>>> ').upper().strip()


def write_to_history(buy):

    buy = customer
    time = datetime.now()
    text = '\n{},{}'.format(buy, time)
    with open('history.txt', 'a') as file:
        file.write(text)


def choice():

    duty = input('\nAre You An Employee Or Customer?? ')
    while not (duty == '1' or duty == '2' or duty == '3'):
        if duty == '1':
            employee()
            exit()
        elif duty == '2':
            get_option()
        elif duty == '3':
            print('Thank You Come Again!!')
            exit()
        else:
            print('Invalid Choice... Please Retype Choice!!')


def main():

    greeting()
    print('--------------------------------------------------------------')
    print('\nEnter:   (1)Employee   (2)Customer   (3)Quit')

    choice()

    get_option()
    buy = customer
    rent = int

    write_to_history(buy)


if __name__ == '__main__':
    main()
