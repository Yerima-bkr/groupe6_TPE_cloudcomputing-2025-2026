# Cette fonction calcule la somme des carrés des chiffres d'un nombre
def somme_carres(n):
    somme = 0                  # On crée une variable pour stocker la somme
    while n > 0:               # Tant que le nombre n'est pas égal à 0
        chiffre = n % 10       # On récupère le dernier chiffre du nombre
        somme = somme + chiffre * chiffre  # On ajoute le carré du chiffre
        n = n // 10            # On enlève le dernier chiffre du nombre
    return somme               # On retourne la somme obtenue

# Cette fonction vérifie si un nombre est heureux
def nombre_heureux(n):
    deja_vus = []              # Liste pour mémoriser les valeurs déjà calculées

    while n != 1:              # Tant que le nombre n'est pas égal à 1
        if n in deja_vus:      # Si le nombre a déjà été vu
            return False       # Le nombre n'est pas heureux
        deja_vus.append(n)     # On ajoute le nombre à la liste
        n = somme_carres(n)    # On calcule la nouvelle valeur

    return True                # Si on arrive à 1, le nombre est heureux

# On demande à l'utilisateur de saisir un nombre limite
n = int(input("Entrer un nombre n : "))  # Lecture du nombre saisi

# On affiche un message à l'écran
print("Les nombres heureux jusqu'à", n, "sont :")  # Titre

# On teste tous les nombres de 1 jusqu'à n
for i in range(1, n + 1):      # Boucle qui parcourt les nombres
    if nombre_heureux(i):      # Si le nombre est heureux
        print(i, end=" ")      # On affiche le nombre
