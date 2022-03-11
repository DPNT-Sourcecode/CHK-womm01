

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    offer_a = 0
    offer_b = 0
    for sku in skus:
        if sku == 'A':
            total = total + 50
            offer_a = offer_a + 1
            if offer_a == 3:
                offer_a = 0
                total = total - 20
        elif sku == 'B':
            total = total + 30
            offer_b = offer_b + 1
            if offer_b == 2:
                offer_b = 0
                total = total - 5
        elif sku == 'C':
            total = total + 20
        elif sku == 'D':
            total = total + 15
        else:
            return -1
    return total






