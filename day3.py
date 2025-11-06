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
    
