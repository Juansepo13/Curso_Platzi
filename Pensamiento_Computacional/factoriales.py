#!/usr/bin/python3
def factorial(n):
    """Calcula el factorial de n.
    n int > 0
    returns n!
    """
    if n == 1:
        return 1

    return n * factorial(n -1)

n = int(input("Escribe un entero: "))

print(factorial(n))
