import math
def sol(a, b, c):
    solution1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    solution2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(solution1, solution2)

sol(48999775, 5143855.04, -61703100)