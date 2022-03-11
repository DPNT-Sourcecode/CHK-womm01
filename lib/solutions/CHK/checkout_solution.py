

# noinspection PyUnusedLocal
# skus = unicode string
import math


def checkout(skus):
    total = 0
    offer_a = 0
    offer_b = 0
    offer_e = 0
    offer_f = 0
    offer_eb = 0
    for sku in skus:
        if sku == 'A':
            total = total + 50
            offer_a = offer_a + 1
        elif sku == 'B':
            total = total + 30
            offer_b = offer_b + 1
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
        elif sku == 'F':
            if offer_f > -1:
                total = total + 10
            offer_f = offer_f + 1
            if offer_f == 2:
                offer_f = -1
        else:
            return -1
    if offer_a > 4:
        tmp = math.floor(offer_a / 5)
        total = total - (50 * tmp)
        offer_a = offer_a % 5
    if offer_a > 2:
        total = total - 20
    if offer_eb > 0 and offer_b > 0:
        if offer_b > offer_eb:
            offer_b = offer_b - offer_eb
            total = total - (30 * offer_eb)
        else:
            total = total - (30 * offer_b)
            offer_b = 0
    if offer_b > 1:
        total = total - (15 * math.floor(offer_b / 2))
    return int(total)





