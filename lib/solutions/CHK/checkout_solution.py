

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    offer_a = 0
    offer_b = 0
    offer_e = 0
    offer_eb = 0
    for sku in skus:
        if sku == 'A':
            total = total + 50
            offer_a = offer_a + 1
            if offer_a == 5:
                offer_a = 0
                total = total - 50
        elif sku == 'B':
            if offer_eb > 0:
                offer_eb = offer_eb - 1
            else:
                offer_b = offer_b + 1
                total = total + 30
            if offer_b == 2:
                offer_b = 0
                total = total - 15
        elif sku == 'C':
            total = total + 20
        elif sku == 'D':
            total = total + 15
        elif sku == 'E':
            total = total + 40
            offer_e = offer_e + 1
            if offer_e == 2:
                offer_e = 0
                offer_eb = offer_eb + 1
        else:
            return -1
    if offer_a > 2:
        total = total - 20
    return total

