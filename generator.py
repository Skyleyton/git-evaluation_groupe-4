#!/usr/bin/env python3

import random
import sys

def generer_expression(n):
    operations = ['+', '-', '*', '/']
    for _ in range(n):
        nombre1 = random.randint(1, 1000)
        nombre2 = random.randint(1, 1000)
        operation = random.choice(operations)
        expression = f"{nombre1}{operation}{nombre2}"
        print(expression)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generator.py <nombre d'expressions>")
    else:
        try:
            nombre_d_expressions = int(sys.argv[1])
            generer_expression(nombre_d_expressions)
        except ValueError:
            print("Erreur: Le nombre d'expressions doit être un entier.")
