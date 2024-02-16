from random import randrange, choice
import sys

# Si la longueur des arguments en ligne de commande est différent de 2 on exit le programme avec le code d'erreur 1.
if (len(sys.argv) != 2):
    print("Usage: python generator.py <n>")
    print("or")
    print("Usage: python3 generator.py <n>")
    sys.exit(1)

# On va gérer les exceptions où l'argument donné n'est pas un chiffre.
try:
    n = int(sys.argv[1])
except ValueError:
    print("Veuillez entrer un nombre !")
    sys.exit(1)

# Un tuple d'opérations, on va utiliser un tuple car on ne va pas changer les valeurs du tuple.
operation_tuple = ('+', '-', '/', '*')

for i in range(n):
    nombre1 = randrange(1, 1000)
    nombre2 = randrange(1, 1000)
    random_op = choice(operation_tuple)

    # L'expression qui va être générée.
    expression = str(nombre1) + random_op + str(nombre2)
    print(expression)
