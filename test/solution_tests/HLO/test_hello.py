from solutions.HLO.hello_solution import hello


class TestHlo:
    def test_hello(self):
        assert 'hello' == hello('Carlos')

