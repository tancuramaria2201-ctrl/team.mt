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
def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a
def is_prime(n):
   
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def fibonacci(n):
   
    if not isinstance(n, int) or n < 0:
        raise ValueError("n має бути невід'ємним цілим")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def is_power_of_five(n):
    
    if not isinstance(n, int) or n < 1:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1