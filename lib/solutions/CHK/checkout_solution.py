

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    for sku in skus:
        total = total + item_value(sku)
    return total


def item_value(sku):
    if sku == 'A':
        return 50
    if sku == 'B':
        return 30
    if sku == 'C':
        return 20
    if sku == 'D':
        return 15
    return -1



