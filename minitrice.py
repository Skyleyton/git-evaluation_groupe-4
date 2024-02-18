#!/usr/bin/env python3

import sys
import re

def calculer(expression):
    # Utilisation d'expressions régulières pour extraire les nombres et l'opérateur
    match = re.fullmatch(r'(\d+(\.\d+)?)(\s*)([+\-*/])(\s*)(\d+(\.\d+)?)', expression)
    if not match:
        return f"Erreur de syntaxe pour le calcul: \"{expression}\""

    nombre1, operateur, nombre2 = match.group(1), match.group(4), match.group(6)
    
    # Convertir les nombres en float ou int selon la présence d'un point décimal
    if '.' in nombre1:
        nombre1 = float(nombre1)
    else:
        nombre1 = int(nombre1)
    
    if '.' in nombre2:
        nombre2 = float(nombre2)
    else:
        nombre2 = int(nombre2)

    # Effectuer le calcul
    if operateur == '+':
        resultat = nombre1 + nombre2
    elif operateur == '-':
        resultat = nombre1 - nombre2
    elif operateur == '*':
        resultat = nombre1 * nombre2
    elif operateur == '/':
        if nombre2 == 0:
            return "Erreur: Division par zéro."
        resultat = nombre1 / nombre2
    else:
        return "Erreur: Opérateur non reconnu."

    # Retourner le résultat formaté
    if isinstance(resultat, float) and resultat.is_integer():
        return str(int(resultat))  # Convertir en int si le résultat est un entier
    elif isinstance(resultat, float):
        return f"{resultat:.2f}"  # Conserver deux chiffres après la virgule si nécessaire
    else:
        return str(resultat)

def main():
    # Lecture de l'entrée standard si des données y sont présentes
    if not sys.stdin.isatty():
        for ligne in sys.stdin:
            print(calculer(ligne.strip()))
    else:
        # Mode interactif
        while True:
            try:
                expression = input("> ")
                if expression.lower() == 'exit':
                    break
                resultat = calculer(expression)
                print(resultat)
            except EOFError:
                print("\nFin des calculs :)")
                break  # Sortie propre du programme lors de la réception d'un EOF (Ctrl + D)

if __name__ == "__main__":
    main()
