import pytest
from calculator import Calculator


class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 2) == 3
        assert calc.get_stack() == [3]

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(4, 2) == 2

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 5) == 10

    def test_divide(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(10, 0)
        assert calc.divide(10, 1) == 10

    def test_power(self):
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.get_last_result() == 8

    def test_square_root_negative_raises(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.square_root(-4)
        assert calc.square_root(4) == 2

    def test_factorial_requires_integer(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.factorial(4.5)
        assert calc.factorial(5) == 120

    def test_memory_store_and_clear(self):
        calc = Calculator()
        calc.memory_store(7)
        assert calc.memory_recall() == 7
        calc.memory_clear()
        assert calc.memory_recall() == 0

    def test_get_last_result_and_clear_stack(self):
        calc = Calculator()
        calc.add(1, 1)
        calc.multiply(2, 3)
        assert calc.get_last_result() == 6
        calc.clear_stack()
        assert calc.get_stack() == []
        calc.add(2, 3)
        assert calc.get_last_result() == 5

    def test_get_last_result_empty(self):
        calc = Calculator()
        assert calc.get_last_result() is None

    def test_negate(self):
        calc = Calculator()
        assert calc.negate(1) == -1

    def test_abs_neg(self):
        calc = Calculator()
        assert calc.absolute(-1) == 1

    def test_abs_pos(self):
        calc = Calculator()
        assert calc.absolute(1) == 1

    def test_modulo(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.modulo(4, 0)
        assert calc.modulo(4, 2) == 0

    def test_is_even(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.is_even(4.5)
        assert calc.is_even(2)

    def test_gcd(self):
        calc = Calculator()
        assert calc.gcd(8, 4) == 4
