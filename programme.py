def calculer(expression):
    # Séparation des nombres et de l'opérateur
    nombre1, operateur, nombre2 = expression.split()

    # Conversion des nombres en flottants
    nombre1 = float(nombre1)
    nombre2 = float(nombre2)

    # Réalisation du calcul
    if operateur == '+':
        resultat = nombre1 + nombre2
    elif operateur == '-':
        resultat = nombre1 - nombre2
    elif operateur == '*':
        resultat = nombre1 * nombre2
    elif operateur == '/':
        if nombre2 != 0:  # Vérification pour éviter la division par zéro
            resultat = nombre1 / nombre2
        else:
            return "Erreur: Division par zéro!"
    else:
        return "Opérateur invalide!"

    return resultat

# Programme principal
while True:
    expression = input("Entrez une expression (nombre1 opérateur nombre2) ou 'exit' pour quitter : ")
    if expression.lower() == 'exit':
        print("Merci d'avoir utilisé le programme. Au revoir!")
        break
    try:
        resultat = calculer(expression)
        print("Résultat:", resultat)
    except Exception as e:
        print("Une erreur s'est produite:", e)
