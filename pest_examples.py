from token import STRING, FSTRING_START


class TestExample:
    def test_check_math(self):
        a = 3
        b = 4
        assert a+b == 7, f"Тут говна поели"

    def test_check_math2(self):
        a = 3
        b = 4
        assert a + b == 7, f"Тут говна поели"

    def test_check_math3(self):
        a = 3
        b = 4
        assert a + b ==7, f"Тут говна поели"

    def test_check_math1(self):
        a = 3
        b = 2
        assert a + b == 8, f"Тут говна поели"

