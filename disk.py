from datetime import datetime


def load_inventory(filename):
    with open(filename) as f:
        f.readline()
        data = f.readlines()
        return data


def save_inventory(inventory):
    with open('inventory.txt', 'w') as f:
        f.write('Vehicle_name, price, stock\n')
        for item in inventory.values():
            f.write('{},{},{}\n'.format(
                item['name'],
                item['price'],
                item['quantity'],
            ))


def total_revenue():
    with open('history.txt') as f:
        rev = 0
        for line in f:
            name, vehicle_name, time, total = line.split('|')
            rev += int(total)

        return rev


def write_to_history(name, buy, total):
    time = datetime.now()
    text = '{} | {} | {} | {}\n'.format(name, buy, time, total)
    with open('history.txt', 'a') as file:
        file.write(text)
