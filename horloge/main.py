import time

def afficher_heure(heure):
    heure_str = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_str)

def regler_heure(heures, minutes, secondes):
    return heures, minutes, secondes

import time

def afficher_heure(heure):
    """
    Affiche l'heure au format hh:mm:ss.
    
    Args:
    - heure (tuple): Tuple contenant les heures, les minutes et les secondes.
    """
    heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format)

def regler_heure():
    """
    Fonction permettant de régler l'heure en demandant à l'utilisateur
    d'entrer les heures, les minutes et les secondes.
    
    Returns:
    - tuple: Tuple contenant les heures, les minutes et les secondes.
    """
    heures = int(input("Entrez les heures : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    return heures, minutes, secondes

def main():
    # Initialisation avec l'heure actuelle
    heure_actuelle = time.localtime()
    heure = (heure_actuelle.tm_hour, heure_actuelle.tm_min, heure_actuelle.tm_sec)

    while True:
        afficher_heure(heure)
        time.sleep(1)  
        heure = time.localtime()
        heure = (heure.tm_hour, heure.tm_min, heure.tm_sec)

if __name__ == "__main__":
    main()
