from core import *
from disk import *
from datetime import datetime


def greeting():
    print('\nWelcome To Henry Fords Rental Agency!!!\n')
    name = input('What Is Your Name? ')
    return name


def choice(name, inv):
    print('--------------------------------------------------------------')
    print('\nEnter:   (1)Employee   (2)Customer   (3)Quit')
    while True:
        duty = input('\nAre You An Employee Or Customer?? ')
        if duty == '1':
            employee()
            choice(name, inv)
            break
        elif duty == '2':
            get_option(name, inv)
            break
        elif duty == '3':
            print('Thank You Come Again!!')
            exit()
        else:
            print('Invalid Choice... Please Retype Choice!!')


def employee():
    inventory = load_inventory('inventory.txt')
    rev = total_revenue()
    print()
    print('(Inventory)   (Revenue)   (History)')
    while True:
        program = input('\nWhat Would You Like To View?? ').upper().strip()
        if program == 'INVENTORY':
            print()
            file = open('inventory.txt', 'r')
            contents = file.read()
            print(contents)
            file.close()
            break
        elif program == 'HISTORY':
            file = open('history.txt', 'r')
            contents = file.read()
            print(contents)
            file.close()
            break
        else:
            print('Invalid Choice... Please Retype Choice')


def get_option(name, inv):
    print('--------------------------------------------------------------')
    print()
    print('      (Rent)           (Return)')

    while True:
        option = input('\nWould your like to rent a Vehicle or return one?'
                       ).upper().strip()
        if option == 'RENT':
            customer(name, inv)
            choice(name, inv)
            break

        elif option == 'RETURN':
            shop(inv)
            print('Thanks for shopping with our Rental Agency Come again!!')
            choice(name, inv)
            exit()
        else:
            print('Invalid Choice... Please Retype Choice!!')
            print()


def shop(inv):
    print('--------------------------------------------------------------')
    print('\n (Ford Truck)  (Chevy Impala)  (Thunderbird)')
    shop = input('\nWhat Vehicle Would you Like to Return? ').upper().strip()
    inventory = inv
    if shop in inv:
        rent = int(input('How many days did you hold this vehicle? '))
        add_stock(inv, shop)
        save_inventory(inventory)
        print('______________________________________')
        print('This vehicle was {} per day..'.format(inv[shop]['price']))
        print('The total amount is {}'.format(inv[shop]['price'] * rent))
        print('______________________________________')

    else:
        print('Invalid Choice... Please Retype Choice!!')
        print()
        rent = input('>>> ').upper().strip()


def customer(name, inv):
    while True:
        print('--------------------------------------------------------------')
        print('\n (Ford Truck)  (Chevy Impala)  (Thunderbird)')
        buy = input('\nWhat Vehicle Would You Like To Rent? ').upper().strip()
        inventory = inv
        if buy in inventory:
            rent = int(input('\nHow Many Days Would You Like To Rent? '))
            print(
                '\nThis Vehicle Will be ${} per day & you have {} days to return it!!'.
                format(inv[buy]['price'], rent))
            rm_stock(inv, buy)
            save_inventory(inventory)

            total = (rent * inv[buy]['price'])
            write_to_history(name, buy, total)
            break

        else:
            print('Invalid Choice... Please Retype Choice!!')


def main():
    raw_data = load_inventory('inventory.txt')
    inv = inventory_data(raw_data)

    name = greeting()

    choice(name, inv)

    buy = customer(name, inv)
    save_inventory()


if __name__ == '__main__':
    main()
