def load_inventory():
    with open('inventory.txt') as f:
        inv = {}
        for line in f:
            name, price_str, quant_str = line.split(',')
            item = {
                'name': name,
                'price': int(price_str),
                'quantity': int(quant_str),
            }
            inv[name] = item
        return inv


def save_inventory(inventory):
    with open('inventory.txt', 'w') as f:
        for item in inventory.values():
            f.write('{},{},{}\n'.format(
                item['name'],
                item['price'],
                item['quantity'],
            ))
