#!/usr/bin/env python3
import sys
import re

def calculer(expression):
    # Utilisation d'expressions régulières pour extraire les nombres et l'opérateur
    match = re.search(r'(\d+(\.\d+)?)(\s*)([+\-*/])(\s*)(\d+(\.\d+)?)', expression)
    if not match:
        return "Erreur: Veuillez entrer une expression valide (nombre opérateur nombre)."
    
    nombre1, operateur, nombre2 = match.group(1), match.group(4), match.group(6)
    
    try:
        nombre1 = float(nombre1)
        nombre2 = float(nombre2)
    except ValueError:
        return "Erreur: Les nombres entrés sont invalides."
    
    # Réalisation du calcul selon l'opérateur
    if operateur == '+':
        return nombre1 + nombre2
    elif operateur == '-':
        return nombre1 - nombre2
    elif operateur == '*':
        return nombre1 * nombre2
    elif operateur == '/':
        if nombre2 == 0:
            return "Erreur: Division par zéro."
        return nombre1 / nombre2
    else:
        return "Erreur: Opérateur non reconnu."

def main():
    # Lecture de l'entrée standard si des données y sont présentes
    if not sys.stdin.isatty():
        for ligne in sys.stdin:
            print(calculer(ligne.strip()))
    else:
        # Mode interactif
        while True:
            try:
                expression = input("Entrez votre calcul (ou tapez 'exit' pour quitter): ")
                if expression.lower() == 'exit':
                    break
                resultat = calculer(expression)
                print(resultat)
            except EOFError:
                break

if __name__ == "__main__":
    main()
