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