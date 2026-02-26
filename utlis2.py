def factorial(n):

    if not isinstance(n, int) or n < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних цілих чисел")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result