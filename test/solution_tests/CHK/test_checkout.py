import pytest

from solutions.CHK.checkout_solution import checkout


class TestChk:
    @pytest.mark.parametrize('skus, result', [['A', 50], ['B', 30], ['C', 20], ['D', 15], ['X', -1]])
    def test_checkout(self, skus, result):
        assert result == checkout(skus)

