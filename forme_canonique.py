from sympy.logic.boolalg import Or, And, Not
from sympy import symbols

def table_de_verite_xor():
    # En-tête de la table
    print("table de vérité\nA\tB\tC")

    # Parcours de toutes les combinaisons possibles de A, B et C (0 ou 1)
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                # Calcul de la valeur de A XOR B XOR C
                resultat = a ^ b ^ c
                # Affichage des valeurs de A, B, C et le résultat
                print(f"{a}\t{b}\t{c}")

# Appel de la fonction pour afficher la table de vérité XOR
table_de_verite_xor()

# Définir les variables d'entrée
A, B, C = symbols('A B C')

# Générer la première forme canonique
premiere_forme_canonique = And(Or(A, B, Not(C)), Or(A, C, Not(B)), Or(B, C, Not(A)))

# Générer la seconde forme canonique
seconde_forme_canonique = Or(And(A, B, C), And(A, Not(B), Not(C)), And(B, Not(A), Not(C)), And(C, Not(A), Not(B)))

# Afficher les formes canoniques
print("Première Forme Canonique :")
print(premiere_forme_canonique)

print("\nSeconde Forme Canonique :")
print(seconde_forme_canonique)
