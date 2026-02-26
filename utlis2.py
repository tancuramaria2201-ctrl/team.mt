def factorial(n):

    if not isinstance(n, int) or n < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних цілих чисел")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 def is_prime(n):
       """Перевіряє, чи є число n простим."""
       if not isinstance(n, int) or n < 2:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True