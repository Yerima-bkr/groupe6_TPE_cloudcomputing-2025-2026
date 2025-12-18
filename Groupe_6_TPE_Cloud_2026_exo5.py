# definition de la fonction 
def compresser_texte(texte):                                 
    if not texte:                                            # Dans le cas où il n'y a pas de texte 
          return ""                                          #elle revoit une liste vide
       
    resultat = ""                                            # affection d'une liste vide au resultat 
    compteur = 1                                             # Initialisation du compteur a 1

    for i in range(1, len(texte)):
        if texte[i] == texte[i - 1]:                         # si la lettre sur l'indice actuele est égale a celle de la suivante on a incrémente le compteur  
            compteur += 1
        else:
            resultat += texte[i - 1] + str(compteur)         # concaténation de la lettre et sont compteur sous forme de chaîne de caractères 
            compteur = 1                                     # Reinisialisation du compteur a 1

    # Ajouter le dernier caractère
    resultat += texte[-1] + str(compteur)
    return resultat                                           #fin de la fonction 

#Demander à l'utilisateur d'entrer un texte
texte_utilisateur = input("Entrez un texte à compresser : ")

texte_compresse = compresser_texte(texte_utilisateur)         # Appel de la fonction 

print("Texte compressé :", texte_compresse)                   # Affichage du résultat 

"""
Exemple :
Si l’utilisateur entre *aaabbcccc*, la sortie sera :
Texte compressé : a3b2c4

"""
