from core import *
from disk import *
from datetime import datetime


def greeting():
    print('\nWelcome To Henry Fords Rental Agency!!!\n')
    name = input('What Is Your Name? ')
    return name


def choice(name):
    print('--------------------------------------------------------------')
    print('\nEnter:   (1)Employee   (2)Customer   (3)Quit')
    duty = input('\nAre You An Employee Or Customer?? ')
    while True:
        if duty == '1':
            employee()
            choice(name)
            break
        elif duty == '2':
            get_option(name)
            break
        elif duty == '3':
            print('Thank You Come Again!!')
            exit()
        else:
            print('Invalid Choice... Please Retype Choice!!')


def employee():
    inventory = load_inventory()
    print()
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


def get_option(name):
    print('--------------------------------------------------------------')
    print()
    print('      (Rent)           (Return)')
    option = input('\nWould your like to rent a Vehicle or return one?\n'
                   ).upper().strip()
    while True:
        if option == 'RENT':
            customer(name)
            choice(name)
            break

        elif option == 'RETURN':
            shop()
            print('Thanks for shopping with our Rental Agency Come again!!')
            exit()


def shop():
    print('--------------------------------------------------------------')
    print('\n (Ford Truck)  (Chevy Impala)  (Thunderbird)')
    shop = input('\nWhat Vehicle Would you Like to Return? ').upper().strip()
    price = get_vehicleprice(shop)
    if shop == 'FORD TRUCK':
        rent = int(input('How many days did you hold this vehicle? '))
        print('______________________________________')
        print('This vehicle was {} per day..'.format(price))
        print('The total amount is {}'.format(price * rent))
        print('______________________________________')
    elif shop == 'CHEVY IMPALA':
        rent = int(input('How many days did you hold this vehicle? '))
        print('______________________________________')
        print('This vehicle was {} per day..'.format(price))
        print('The total amount is {}'.format(price * rent))
        print('______________________________________')
    elif buy == 'THUNDERBIRD':
        rent = int(input('How many days did you hold this vehicle? '))
        print('______________________________________')
        print('This vehicle was {} per day..'.format(price))
        print('The total amount is {}'.format(price * rent))
        print('______________________________________')
    else:
        print('Invalid Choice... Please Retype Choice!!')
        print()
        rent = input('>>> ').upper().strip()


def write_to_history2():
    time = datetime.now()


def customer(name):
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
    else:
        print('Invalid Choice... Please Retype Choice!!')
        print()
        buy = input('>>> ').upper().strip()
    total = (rent * price)
    write_to_history(name, buy, total)

    return buy
    return price
    return total


def write_to_history(name, buy, total):

    time = datetime.now()
    text = '\n{} | {} | {} | {}'.format(name, buy, time, total)
    with open('history.txt', 'a') as file:
        file.write(text)


def main():

    name = greeting()

    choice(name)

    buy = customer(name)


if __name__ == '__main__':
    main()
