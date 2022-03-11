import pytest

from solutions.CHK.checkout_solution import checkout


class TestChk:
    @pytest.mark.parametrize('skus, result', [
        ['A', 50], ['B', 30], ['C', 20], ['D', 15], ['EEEEBB', 160]
        ['EE', 80], ['EEE', 80], ['EEEEEE', 160], ['A'*6, 250],
        ["", 0], ["A"*8, 330], ["ABCD", 115], ["AxA", -1], ["AAA", 130], ['BBBB', 90]
    ])
    def test_checkout(self, skus, result):
        assert result == checkout(skus)





