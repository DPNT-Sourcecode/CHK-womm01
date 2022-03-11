import pytest

from solutions.CHK.checkout_solution import checkout


class TestChk:
    @pytest.mark.parametrize('sku, result', [['A', 12], ['X', -1]])
    def test_checkout(self, sku, result):
        assert 'Hello, Carlos!' == checkout('Carlos')
