import time
import random
from colorama import Fore, Back, Style

gg = r"""
   _____  _____ 
  / ____|/ ____|
 | |  __| |  __ 
 | | |_ | | |_ |
 | |__| | |__| |
  \_____|\_____|
"""

perdu = r"""
  _____             _   
 |  __ \           | |                  
 | |__) |__ _ __ __| |_   _             
 |  ___/ _ \ '__/ _` | | | |            
 | |  |  __/ | | (_| | |_| |  _   _   _ 
 |_|   \___|_|  \__,_|\__,_| (_) (_) (_)

"""

#---------------------------------------------#

filin = open("mots.txt", "r")
lignes = filin.readlines()

nbr_lignes = 0
for i in range(len(lignes)):
    nbr_lignes += 1

place = random.randint(0, nbr_lignes)
choix = lignes[place-1]

choix = choix.strip('\n')

filin.close()

#---------------------------------------------#

def afficher(vrai, test):
    dic = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0
    }
    for i in range(len(vrai)):
        dic[vrai[i]] += 1
    for i in range(len(vrai)):
        if vrai[i] == test[i]:
            print(Back.RED + test[i], end="")
            dic[vrai[i]] -= 1
        elif test[i] in vrai:
            for j in range(len(vrai)):
                if vrai[j] == test[j]:
                    dic[vrai[j]] -= 1
            if dic[test[i]] > 0:
                print(Back.YELLOW + test[i], end="")
                dic[test[i]] -= 1
            else:
                print(Back.BLUE + test[i], end="")
        else:
            print(Back.BLUE + test[i], end="")
    print(Style.RESET_ALL)

#---------------------------------------------#

print("")

mot = []
for i in range(len(choix)):
    mot.append(choix[i])

# J'ai vu que jusqu'en 2009 ils donnaient la première lettre du mot
# Après 2009 ils la première et une autre mais sur 6 lettres ça me semble trop simple
print(mot[0],"_ _ _ _ _" )
print("")

choix = []
erreur = 0

while erreur < 8 and choix != mot:
    nouv = input("Quel mot de six lettres est le mot mystère : ")
    while len(nouv) != 6:
        nouv = input("Quel mot de SIX lettres est le mot mystère : ")
    for i in range(len(mot)):
        choix.append(nouv[i])
    if choix != mot:
        erreur += 1
        if erreur == 1:
            choix1 = choix.copy()
            print("")
            afficher(mot, choix1)
            print("")
        elif erreur == 2:
            choix2 = choix.copy()
            print("")
            afficher(mot, choix1)
            afficher(mot, choix2)
            print("")
        elif erreur == 3:
            choix3 = choix.copy()
            print("")
            afficher(mot, choix1)
            afficher(mot, choix2)
            afficher(mot, choix3)
            print("")
        elif erreur == 4:
            choix4 = choix.copy()
            print("")
            afficher(mot, choix1)
            afficher(mot, choix2)
            afficher(mot, choix3)
            afficher(mot, choix4)
            print("")
        elif erreur == 5:
            choix5 = choix.copy()
            print("")
            afficher(mot, choix1)
            afficher(mot, choix2)
            afficher(mot, choix3)
            afficher(mot, choix4)
            afficher(mot, choix5)
            print("")
        elif erreur == 6:
            choix6 = choix.copy()
            print("")
            afficher(mot, choix1)
            afficher(mot, choix2)
            afficher(mot, choix3)
            afficher(mot, choix4)
            afficher(mot, choix5)
            afficher(mot, choix6)
            print("")
        elif erreur == 7:
            choix7 = choix.copy()
            print("")
            afficher(mot, choix1)
            afficher(mot, choix2)
            afficher(mot, choix3)
            afficher(mot, choix4)
            afficher(mot, choix5)
            afficher(mot, choix6)
            afficher(mot, choix7)
            print("")
        choix = []

if erreur != 8:
    print(gg)
    print("Le mot était bien : ", end="")
    for i in range(len(mot)):
        print(mot[i], end='')    
else:
    print(perdu)
    print("Le mot était : ", end="")
    for i in range(len(mot)):
        print(mot[i], end='')    

print("")
print("")
