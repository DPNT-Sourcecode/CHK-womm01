import pytest

from solutions.CHK.checkout_solution import checkout


class TestChk:
    @pytest.mark.parametrize('skus, result', [
        ['A', 50], ['B', 30], ['C', 20], ['D', 15], ['X', -1], ["", 0], ["AA", 100], ["ABCD", 115], ["AxA", 49], ["AAAA", 200]
    ])
    def test_checkout(self, skus, result):
        assert result == checkout(skus)



