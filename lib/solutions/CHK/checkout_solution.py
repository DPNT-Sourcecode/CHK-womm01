# noinspection PyUnusedLocal
# skus = unicode string
import math


def special_discount(counter, limit, price):
    return price * math.floor(counter / limit)


def max_discount(counter, max_limit, min_limit, max_price, min_price):
    discount = 0
    if counter > (max_limit - 1):
        discount = special_discount(counter, max_limit, max_price)
        counter = counter % max_limit
    return discount + special_discount(counter, min_limit, min_price)


def free_discount(counter, freebie):
    if counter > freebie:
        return counter - freebie
    return 0


def any_buy_discount(counter_z, counter_yst, counter_x):
    total = (counter_z + counter_yst + counter_x) / 3 * 45
    free = (counter_z + counter_yst + counter_x) % 3
    if counter_x >= free:
        return (counter_x % 3) * 17 + total
    elif counter_yst >= free - counter_x:
        return (counter_yst % 3) * 20 + counter_x * 17 + total
    return (counter_z % 3) * 21 + counter_yst * 20 + counter_x * 17 + total


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
    offer_u = 0
    offer_n = 0
    offer_m = 0
    offer_r = 0
    offer_sty = 0
    offer_x = 0
    offer_z = 0
    for sku in skus:
        if sku == 'A':
            total = total + 50
            offer_a = offer_a + 1
        elif sku == 'B':
            offer_b = offer_b + 1
        elif sku == 'C':
            total = total + 20
        elif sku == 'D':
            total = total + 15
        elif sku == 'E':
            total = total + 40
            offer_e = offer_e + 1
        elif sku == 'F':
            offer_f = offer_f + 1
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
            offer_m = offer_m + 1
        elif sku == 'N':
            total = total + 40
            offer_n = offer_n + 1
        elif sku == 'O':
            total = total + 10
        elif sku == 'P':
            total = total + 50
            offer_p = offer_p + 1
        elif sku == 'Q':
            offer_q = offer_q + 1
        elif sku == 'R':
            total = total + 50
            offer_r = offer_r + 1
        elif sku == 'S':
            offer_sty = offer_sty + 1
        elif sku == 'T':
            offer_sty = offer_sty + 1
        elif sku == 'U':
            offer_u = offer_u + 1
        elif sku == 'V':
            total = total + 50
            offer_v = offer_v + 1
        elif sku == 'W':
            total = total + 20
        elif sku == 'X':
            offer_x = offer_x + 1
        elif sku == 'Y':
            offer_sty = offer_sty + 1
        elif sku == 'Z':
            offer_z = offer_z + 1
        else:
            return -1

    discount = max_discount(offer_a, 5, 3, 50, 20) + max_discount(offer_h, 10, 5, 20, 5) + max_discount(
        offer_v, 3, 2, 20, 10
    )
    offer_b = free_discount(offer_b, math.floor(offer_e/2))
    offer_f = free_discount(offer_f, math.floor(offer_f/3))
    offer_m = free_discount(offer_m, math.floor(offer_n/3))
    offer_q = free_discount(offer_q, math.floor(offer_r/3))
    offer_u = free_discount(offer_u, math.floor(offer_u/4))
    total = total + offer_b * 30 + offer_f * 10 + offer_m * 15 + offer_u * 40 + offer_q * 30

    if offer_b > 1:
        total = total - special_discount(offer_b, 2, 15)
    if offer_k > 1:
        total = total - special_discount(offer_k, 2, 10)
    if offer_p > 4:
        total = total - special_discount(offer_p, 5, 50)
    if offer_q > 2:
        total = total - special_discount(offer_q, 3, 10)

    return int(any_buy_discount(offer_z, offer_sty, offer_x) + total - discount)


