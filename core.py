from disk import *
from shell import *


def inventory_data(raw_data):
    inv = {}
    for line in raw_data:
        name, price_str, quant_str = line.split(',')
        item = {
            'name': name,
            'price': int(price_str),
            'quantity': int(quant_str),
        }
        inv[name] = item
    return inv


def rm_stock(inv, item):
    inv[item]['quantity'] -= 1
    return inv[item]['quantity']


def add_stock(inv, item):
    inv[item]['quantity'] += 1
    return inv[item]['quantity']
