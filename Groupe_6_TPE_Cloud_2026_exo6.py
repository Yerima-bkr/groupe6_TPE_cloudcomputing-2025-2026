def est_ip_valide(ip):
    """
    Vérifie si une adresse IP est valide.
    
    :param ip: L'adresse IP à vérifier.
    :return: True si l'adresse IP est valide, False sinon.
    """
    # Diviser l'adresse IP en parties
    parties = ip.split(".")
    
    # Vérifier le nombre de parties
    if len(parties) != 4:
        return False
    
    # Vérifier chaque partie
    for partie in parties:
        # Vérifier que la partie est un nombre entier
        if not partie.isdigit():
            return False
        
        # Vérifier que la partie est comprise entre 0 et 255
        if int(partie) < 0 or int(partie) > 255:
            return False
    
    # Si toutes les vérifications sont réussies, l'adresse IP est valide
    return True

def main():
    # Demander à l'utilisateur d'entrer une adresse IP
    ip = input("Entrez une adresse IP : ")
    
    # Vérifier si l'adresse IP est valide
    if est_ip_valide(ip):
        print(f"L'adresse IP {ip} est valide.")
    else:
        print(f"L'adresse IP {ip} est invalide.")

if __name__ == "__main__":
    main()