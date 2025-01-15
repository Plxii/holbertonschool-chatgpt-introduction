#!/usr/bin/python3
import sys

"""
    Calcul du factoriel d'un nombre de manière récursive.

    Description :
    Cette fonction calcule le factoriel d'un nombre entier donné en utilisant une méthode récursive.
    Le factoriel d'un nombre n (noté n!) est défini comme le produit de tous les entiers positifs
    jusqu'à n (n! = n * (n-1) * ... * 1). Par convention, 0! = 1.

    Paramètres :
    - n (int) : Le nombre entier pour lequel calculer le factoriel. Doit être >= 0.

    Retour :
    - int : Le résultat du factoriel de n.
    """

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
