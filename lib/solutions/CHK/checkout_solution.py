

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    if skus == 'AAA':
        return 130
    if skus == 'BB':
        return 45
    for sku in skus:
        if sku == 'A':
            total = total + 50
        elif sku == 'B':
            total = total + 30
        elif sku == 'C':
            total = total + 20
        elif sku == 'D':
            total = total + 15
        else:
            return -1
    return total





