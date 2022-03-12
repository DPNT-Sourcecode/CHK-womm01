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
    offer_m = 0
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
            # total = total + 15
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
            total = total + 30
        elif sku == 'T':
            total = total + 20
        elif sku == 'U':
            # total = total + 40
            offer_u = offer_u + 1
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

    discount = max_discount(offer_a, 5, 3, 50, 20) + max_discount(offer_h, 10, 5, 20, 5) + max_discount(
        offer_v, 3, 2, 20, 10
    )
    offer_b = free_discount(offer_b, math.floor(offer_e/2))
    offer_f = free_discount(offer_f, math.floor(offer_f/2))
    offer_m = free_discount(offer_m, math.floor(offer_n/3))
    offer_q = free_discount(offer_q, math.floor(offer_r/3))
    offer_u = free_discount(offer_u, math.floor(offer_u/3))
    total = total + offer_b * 30 + offer_f * 10 + offer_m * 15 + offer_u * 40 + offer_q * 30
    # if offer_eb > 0 and offer_b > 0:
    #     if offer_b > offer_eb:
    #         offer_b = offer_b - offer_eb
    #         total = total - (30 * offer_eb)
    #     else:
    #         total = total - (30 * offer_b)
    #         offer_b = 0
    # if offer_rq > 0 and offer_q > 0:
    #     if offer_q > offer_rq:
    #         offer_q = offer_q - offer_rq
    #         total = total - (30 * offer_rq)
    #     else:
    #         total = total - (30 * offer_q)
    #         offer_q = 0
    # if offer_nm > 0 and offer_m > 0:
    #     if offer_m > offer_nm:
    #         total = total - (15 * offer_nm)
    #     else:
    #         total = total - (15 * offer_m)
    if offer_b > 1:
        total = total - special_discount(offer_b, 2, 15)
    if offer_k > 1:
        total = total - special_discount(offer_k, 2, 10)
    if offer_p > 4:
        total = total - special_discount(offer_p, 5, 50)
    if offer_q > 2:
        total = total - special_discount(offer_q, 3, 10)
    return int(total - discount)





