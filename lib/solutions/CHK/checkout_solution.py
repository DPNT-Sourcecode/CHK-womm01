

# noinspection PyUnusedLocal
# skus = unicode string
import math


def checkout(skus):
    total = 0
    offer_a = 0
    offer_b = 0
    offer_e = 0
    offer_f = 0
    offer_h = 0
    offer_k = 0
    offer_p = 0
    offer_q = 0
    offer_v = 0
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
        elif sku == 'G':
            total = total + 20
        elif sku == 'H':
            total = total + 10
            offer_h = offer_h + 1
        elif sku == 'I':
            total = total + 35
        elif sku == 'J':
            total = total + 60
        elif sku == 'K':
            total = total + 80
            offer_k = offer_k + 1
        elif sku == 'L':
            total = total + 90
        elif sku == 'M':
            total = total + 15
        elif sku == 'N':
            total = total + 40
        elif sku == 'O':
            total = total + 10
        elif sku == 'P':
            total = total + 50
            offer_p = offer_p + 1
        elif sku == 'Q':
            total = total + 30
            offer_q = offer_q + 1
        elif sku == 'R':
            total = total + 50
        elif sku == 'S':
            total = total + 30
        elif sku == 'T':
            total = total + 20
        elif sku == 'U':
            total = total + 40
        elif sku == 'V':
            total = total + 50
            offer_v = offer_v + 1
        elif sku == 'W':
            total = total + 20
        elif sku == 'X':
            total = total + 90
        elif sku == 'Y':
            total = total + 10
        elif sku == 'Z':
            total = total + 50
        else:
            return -1
    if offer_a > 4:
        tmp = math.floor(offer_a / 5)
        total = total - (50 * tmp)
        offer_a = offer_a % 5
    if offer_a > 2:
        total = total - 20
    if offer_h > 9:
        tmp = math.floor(offer_h / 10)
        total = total - (20 * tmp)
        offer_h = offer_h % 10
    if offer_h > 4:
        total = total - 5
    if offer_v > 2:
        tmp = math.floor(offer_v / 3)
        total = total - (20 * tmp)
        offer_v = offer_v % 3
    if offer_v > 1:
        total = total - 10
    if offer_eb > 0 and offer_b > 0:
        if offer_b > offer_eb:
            offer_b = offer_b - offer_eb
            total = total - (30 * offer_eb)
        else:
            total = total - (30 * offer_b)
            offer_b = 0
    if offer_b > 1:
        total = total - (15 * math.floor(offer_b / 2))
    if offer_k > 1:
        total = total - (10 * math.floor(offer_k / 2))
    if offer_p > 4:
        total = total - (50 * math.floor(offer_p / 5))
    if offer_q > 2:
        total = total - (10 * math.floor(offer_q / 3))
    return int(total)




