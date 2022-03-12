import pytest

from solutions.CHK.checkout_solution import checkout


class TestChk:
    @pytest.mark.parametrize('skus, result', [
        ['A', 50], ['B', 30], ['C', 20], ['D', 15], ['F'*4, 30], ['F'*6, 40], ['EEEEBB', 160], ['EE', 80], ['A'*6, 250],
        ["", 0], ["A"*8, 330], ["ABCD", 115], ["AxA", -1], ["AAA", 130], ['BBBB', 90], ['BEBEEE', 160],
        ['ABCDECBAABCABBAAAEEAA', 665], ['ABCDEABCDE', 280], ['H'*11, 90], ['H'*16, 135], ['KK', 150], ['KKK', 230],
        ['P'*6, 250], ['P'*9, 400], ['Q'*3, 80], ['Q'*5, 140], ['V'*4, 180], ['V'*5, 220], ['U'*4, 120], ['U'*9, 280],
        ['NNN', 120], ['NNNMNNN', 240], ['RRRQQ', 180], ['RRRQQQ', 210],
        ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2, 1880],
        ['LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH', 1880]

    ])
    def test_checkout(self, skus, result):
        assert checkout(skus) == result
