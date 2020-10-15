# On importe une librairie pour choisir un nombre aleatoire :
import random

# On cree une variable nombre_cacher
# On y stock un nombre aleatoire en entre 0 et 100
# on fait appel a la fonction randint qui se trouve dans random 
nombre_cacher = random.randint(0, 100)

print("Tape un nombre entre 0 et 100")

entree_joueur = int( input(">>") )


if entree_joueur < nombre_cacher:
    print("Le nombre est petit")
    
elif entree_joueur > nombre_cacher:
    print("Le nombre est grand")
    
else :
    print("Bravo le nombre est bon")

