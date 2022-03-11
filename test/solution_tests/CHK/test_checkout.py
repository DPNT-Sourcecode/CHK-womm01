import pytest

from solutions.CHK.checkout_solution import checkout


class TestChk:
    @pytest.mark.parametrize('skus, result', [
        ['A', 50], ['B', 30], ['C', 20], ['D', 15], ['EE', 80], ['EEE', 80], ['EEEEEE', 160], ['AAAAAA', 260], ["", 0], ["AAAAAAAA", 330], ["ABCD", 115], ["AxA", -1], ["AAA", 130], ['BBBB', 90]
    ])
    def test_checkout(self, skus, result):
        assert result == checkout(skus)



