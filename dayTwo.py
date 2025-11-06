#notion de type de variable 
#type de variable en python

# 1- les types entiers (integer)
nombre = 24

print(type(nombre))

# 2- les types décimaux (float)
nbr_dcm = 5.9
print (type(nbr_dcm))

# 3- les types complexes
z = 2 + 3j
print(z.real)  # 2.0 → partie réelle, la fonction real
print(z.imag)  # 3.0 → partie imaginaire, lafonction imag

# 4- les types chaines de caractères string/char
nom = "Alice"
print(type(nom))

# 5- les types boolean
est_masculin = False
print (type(est_masculin))

# 6- les types listes qui sont sous formes de tableau en C/C++
notes = [12, 15, 18, 10]
noms = ["Alice", "Bob", "Chloé"]
melange = [10, "Python", True]
 
print(melange)

notes.append(20)     # Ajoute un élément
notes.remove(10)     # Supprime un élément
print(notes[0])      # Premier élément
print(len(notes))    # Longueur de la liste


# 7- les types tuples sont une collection ordonnée mais non modifiable.
coordonnees = (10, 20)
couleurs = ("rouge", "vert", "bleu")
print(coordonnees[1])

# 8- les types dict dictionnaire
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}
print('voici la valeur du type dict ayant pour clé age')
print(personne['age'])

# 9- le type coordonnée est un ensemble est une collection non ordonnée et sans doublons.
couleurs = {"rouge", "vert", "bleu", "rouge"}
print(couleurs)  # {'rouge', 'vert', 'bleu'}

#application
nbr1 = 25
nbr2 = "15"

add = nbr1 + int(nbr2)

print("La somme des deux nombres est : " + str(add))

