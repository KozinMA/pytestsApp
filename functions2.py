# Козин М.А.
from math import sqrt

def multiplication(x, y):
    return x * y

def division(x, y):
    if (y == 0):
        return "На 0 делить нельзя!"
    return x / y

def distance_between_two_points( x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def quadratic_equation(a, b, c):
    D = b * b - 4 * a * c
    a_2 = 2 * a
    if (D < 0):
        return "Действительных корней нет"
    if (D == 0):
        return f"Корнем этого уравнения является {-(b / a_2)}"
    sqrt_D = sqrt(D)
    x1 = (-b - sqrt_D) / a_2
    x2 = (-b + sqrt_D) / a_2
    return f"Корнями этого уравнения являются {x1} и {x2}"

def sum_of_geometric_progression(a1, q, n):
    if (q == 1):
        return n * a1
    qn = pow(q,n)
    return a1 * ((qn - 1)/(q - 1))

def number_words(str):
    words = 0
    whitespace = 0
    for i in range(0, len(str)):
        if ((str[i] == " " and whitespace < 1) or (str[i] == ".")):
            words += 1
            whitespace += 1
        else:
            while(str[i] == " " and i < len(str)):
                i += 1
            whitespace = 0
    return words

def search_substring_in_string(substring, string):
    p = len(substring)
    s = len(string)
    if (substring[p - 1] == string[s - 1] and p == s):
        return f'Подстрока "{substring}" присутствует в строке'
    else: "Такой подстроки нет"

    for i in range(0, s): 
        for j in range(0, p):
            if (substring[j] != string[i + j]): break
        if (j == p - 1):
            return f'Подстрока "{substring}" присутствует в строке'
    return "Такой подстроки нет"
    
def conversion_to_uppercase(text):
    return text.upper()