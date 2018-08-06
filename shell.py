from core import *
from disk import *
from datetime import datetime


def greeting():
    print('\nWelcome To Henry Fords Rental Agency!!!\n')
    name = input('What Is Your Name? ')


def choice():
    print('--------------------------------------------------------------')
    print('\nEnter:   (1)Employee   (2)Customer   (3)Quit')
    duty = input('\nAre You An Employee Or Customer?? ')
    while True:
        if duty == '1':
            employee()
            break
        elif duty == '2':
            get_option()
            break
        elif duty == '3':
            print('Thank You Come Again!!')
            exit()
        else:
            print('Invalid Choice... Please Retype Choice!!')


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
    while True:
        if option == 'RENT':
            customer()
            choice()
            break

        elif option == 'RETURN':
            print('thanks for shopping with our Rental Agency Come again!!')
            choice()
            break


def customer():

    print('--------------------------------------------------------------')
    print('\n (Ford Truck)  (Chevy Impala)  (Thunderbird)')
    buy = input('\nWhat Vehicle Would You Like To Rent? ').upper().strip()
    price = get_vehicleprice(buy)
    if buy == 'FORD TRUCK':
        rent = int(input('\nHow Many Days Would You Like To Rent? '))
        print(
            '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
            format(price, rent))
    elif buy == 'CHEVY IMPALA':
        rent = int(input('\nHow Many Days Would You Like To Rent? '))
        print(
            '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
            format(price, rent))
    elif buy == 'THUNDERBIRD':
        rent = int(input('\nHow Many Days Would You Like To Rent? '))
        print(
            '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
            format(price, rent))
        print('Invalid Choice... Please Retype Choice!!')
        print()
        buy = input('>>> ').upper().strip()
    total = (rent * price)
    write_to_history(buy, price, total)

    return buy
    return price
    return total


def write_to_history(buy, price, total):
    time = datetime.now()
    text = '\n{}, {}, {}, {}'.format(buy, time, price, total)
    with open('history.txt', 'a') as file:
        file.write(text)


def main():

    greeting()

    choice()

    buy = customer()


if __name__ == '__main__':
    main()
