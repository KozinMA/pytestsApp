# Козин М.А.
import functions3
import pytest
class TestMathFunctions:   
    @pytest.mark.parametrize("multiplier1, multiplier2, expected_result", [
        (10, 5, 50),
        (0.5, 3, 1.5),
        (-3, -2, 6),
        (-8, 5, -40),
        (0.3, 0.2, 0.06)
    ])
    def test_multiplication(self, multiplier1, multiplier2, expected_result):
        assert functions3.multiplication(multiplier1, multiplier2) == expected_result
   
    @pytest.mark.parametrize("divisible, divider, expected_result", [
        (30, 2, 15),
        (1.5, 3, 0.5),
        (-5, -1, 5),
        (432, 0, "На 0 делить нельзя!"),
        (5, 2, 2.5)
    ])
    def test_division(self, divisible, divider, expected_result):
        assert functions3.division(divisible, divider) == expected_result

    @pytest.mark.parametrize("x1, y1, x2, y2, expected_result", [
        (0, 0, 0, 0, 0),
        (0.3, -8, 0.5, -8, 0.2),
        (0, -2, 0, 2, 4),
        (3, -4, 6, -8, 5),
        (10, -3, 18, 3, 10)
    ])
    def test_distance_between_two_points(self, x1, y1, x2, y2, expected_result):
        assert functions3.distance_between_two_points(x1, y1, x2, y2) == expected_result

    @pytest.mark.parametrize("a, b, c, expected_result", [
        (50, 1, 20, "Действительных корней нет"),
        (-5, 0.2, -8, "Действительных корней нет"),
        (2, 4, 2, "Корнем этого уравнения является -1.0"),
        (-0.5, 2, 6, "Корнями этого уравнения являются 6.0 и -2.0"),
        (0.25, -10, 75, "Корнями этого уравнения являются 10.0 и 30.0")
    ])
    def test_quadratic_equation(self, a, b, c, expected_result):
        assert functions3.quadratic_equation(a, b, c) == expected_result
        
    @pytest.mark.parametrize("a1, q, n, expected_result", [
        (4, 1, 3, 12),
        (0.2, 3, 3, 2.6),
        (-10, 1, 2, -20),
        (-0.5, 3, 2, -2),
        (5, -3, 2, -10.0)
    ])
    def test_sum_of_geometric_progression(self, a1, q, n, expected_result):
        assert functions3.sum_of_geometric_progression(a1, q, n) == expected_result