# Козин М.А.
import functions2
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
        assert functions2.multiplication(multiplier1, multiplier2) == expected_result
   
    @pytest.mark.parametrize("divisible, divider, expected_result", [
        (30, 2, 15),
        (1.5, 3, 0.5),
        (-5, -1, 5),
        (432, 0, "На 0 делить нельзя!"),
        (5, 2, 2.5)
    ])
    def test_division(self, divisible, divider, expected_result):
        assert functions2.division(divisible, divider) == expected_result

    @pytest.mark.parametrize("x1, y1, x2, y2, expected_result", [
        (0, 0, 0, 0, 0),
        (0.3, -8, 0.5, -8, 0.2),
        (0, -2, 0, 2, 4),
        (3, -4, 6, -8, 5),
        (10, -3, 18, 3, 10)
    ])
    def test_distance_between_two_points(self, x1, y1, x2, y2, expected_result):
        assert functions2.distance_between_two_points(x1, y1, x2, y2) == expected_result

    @pytest.mark.parametrize("a, b, c, expected_result", [
        (50, 1, 20, "Действительных корней нет"),
        (-5, 0.2, -8, "Действительных корней нет"),
        (2, 4, 2, "Корнем этого уравнения является -1.0"),
        (-0.5, 2, 6, "Корнями этого уравнения являются 6.0 и -2.0"),
        (0.25, -10, 75, "Корнями этого уравнения являются 10.0 и 30.0")
    ])
    def test_quadratic_equation(self, a, b, c, expected_result):
        assert functions2.quadratic_equation(a, b, c) == expected_result
        
    @pytest.mark.parametrize("a1, q, n, expected_result", [
        (4, 1, 3, 12),
        (0.2, 3, 3, 2.6),
        (-10, 1, 2, -20),
        (-0.5, 3, 2, -2),
        (5, -3, 2, -10.0)
    ])
    def test_sum_of_geometric_progression(self, a1, q, n, expected_result):
        assert functions2.sum_of_geometric_progression(a1, q, n) == expected_result

class TestStrFunctions:
    @pytest.fixture
    def text_file(self):
        with open("strsFile.txt", encoding='utf8') as f:
            text = f.read()
            return text
    
    @pytest.mark.parametrize("expected_result", [33])    
    def test_number_words(self, text_file, expected_result):
        assert functions2.number_words(text_file) == expected_result

    @pytest.mark.parametrize("substring, expected_result", [
        ("дач", 'Подстрока "дач" присутствует в строке'),
        ("вода", 'Подстрока "вода" присутствует в строке'),
        ("ок", 'Подстрока "ок" присутствует в строке'),
        ("32ок", "Такой подстроки нет"),
        ("символами", "Такой подстроки нет")
    ])    
    def test_search_substring_in_string(self, substring, text_file, expected_result):
        assert functions2.search_substring_in_string(substring, text_file) == expected_result

    @pytest.mark.parametrize("expected_result", ["ОДНОЙ ИЗ РАСПРОСТРАНЕННЫХ ЗАДАЧ ПРИ РАБОТЕ СО СТРОКАМИ В PYTHON ЯВЛЯЕТСЯ ПРЕОБРАЗОВАНИЕ ВСЕХ СИМВОЛОВ СТРОКИ В ВЕРХНИЙ РЕГИСТР. ВОЗМОЖНО, ЭТО МОЖЕТ ПОТРЕБОВАТЬСЯ ПРИ ФОРМАТИРОВАНИИ ВЫВОДА НА ЭКРАН ИЛИ ПРИ ОБРАБОТКЕ ДАННЫХ, ВВЕДЕННЫХ ПОЛЬЗОВАТЕЛЕМ."])  
    def test_conversion_to_uppercase(self, text_file, expected_result):
        assert functions2.conversion_to_uppercase(text_file) == expected_result