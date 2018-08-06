from disk import *
from shell import *


def Load_inventory():
    inventory = [{
        'Name': 'FORD TRUCK',
        'stock': 6,
        'price': 210,
        'replacement cost': 2500
    }, {
        'Name': 'CHEVY IMPALA',
        'stock': 3,
        'price': 120,
        'replacement cost': 1500
    }, {
        'Name': 'THUNDERBIRD',
        'stock': 4,
        'price': 150,
        'replacement cost': 2100
    }]


def get_vehicleprice(buy):
    if buy == 'FORD TRUCK':
        price = 210
    if buy == 'CHEVY IMPALA':
        price = 120
    if buy == 'THUNDERBIRD':
        price = 150

    return price
