

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    return [value(sku) in skus]


def value(sku):
    if sku == 'A':
        return 50
    if sku == 'B':
        return 30
    if sku == 'C':
        return 20
    if sku == 'D':
        return 15
    return -1


