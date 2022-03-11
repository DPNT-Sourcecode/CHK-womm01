import pytest

from solutions.CHK.checkout_solution import checkout


class TestChk:
    @pytest.mark.parametrize('skus, result', [
        ['A', 50], ['B', 30], ['C', 20], ['D', 15], ['EEEEBB', 145], ['EE', 80], ['A'*6, 250],
        ["", 0], ["A"*8, 330], ["ABCD", 115], ["AxA", -1], ["AAA", 130], ['BBBB', 90], ['BEBEEE', 145],
        ['ABCDECBAABCABBAAAEEAA', 665]
    ])
    def test_checkout(self, skus, result):
        assert checkout(skus) == result


