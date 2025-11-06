# Exercice 1, opérations mathématiques sur deux nombres
nombre1 = float(input('entrez le premier nombre')) 
nombre2 = float(input('entrez le deuxième nombre'))

# addition
print('la somme de vos nombres est :', nombre1 + nombre2)
# soustraction
print('la différence de vos nombres est :', nombre1 - nombre2)
# multiplication
print('le produit de vos nombres est :', nombre1 * nombre2)
# division
print('le quotient de vos nombres est :', nombre1 // nombre2)
# le reste de la division
print('le reste de la division de vos nombres est :', nombre1 % nombre2)
# Exercice 2, Écris un programme qui demande un entier x et qui affiche en Python
nbEntier = int(input('entrez un nombre entier'))
print('Le carré de', nbEntier, 'est', nbEntier ** 2)
#Vérification du nombre pair ou impair
if nbEntier % 2 == 0:
    print(nbEntier, 'est un nombre pair')
else:
    print(nbEntier, 'est un nombre impair')

#Vérification du nombre entre 10 et 50
if 10 <= nbEntier <= 50:
    print(nbEntier, 'est compris entre 10 et 50')
else:
    print(nbEntier, 'n\'est pas compris entre 10 et 50')

# s’il est divisible par 3 et 5
if nbEntier % 3 == 0 and nbEntier % 5 == 0:
    print(nbEntier, 'est divisible par 3 et 5')
else:
    print(nbEntier, 'n\'est pas divisible par 3 et 5')

# création d'une liste et vérification d'appartenance 
prenom = input('entrez votre prénom')
liste_prenoms = ['Alice', 'Bob', 'Chloé', 'David']
if prenom in liste_prenoms:
    print(prenom, 'est dans la liste')