import csv
import time
import datetime

"""
logo = 
  __  __       _    _             _____           _       
 |  \/  |     | |  | |           / ____|         (_)      
 | \  / | __ _| | _| |__  _   _ | |     ___   ___ _  __ _ 
 | |\/| |/ _` | |/ / '_ \| | | || |    / _ \ / __| |/ _` |
 | |  | | (_| |   <| |_) | |_| || |___| (_) | (__| | (_| |
 |_|  |_|\__,_|_|\_\_.__/ \__, | \_____\___/ \___|_|\__,_|
                            __/ |                          
                           |___/                           

        "Votre partenaire financier de confiance"
    
print(logo)

"""

# Appel de la fonction pour afficher le logo de la banque avec la devise
def get_last_row(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        derniere_info = file.readlines()[-1] 
        return derniere_info.split(",")

# Lire le fichier CSV et récupérer la dernière ligne
infos = get_last_row("GestionArgent\stats.csv")
print(infos)

if infos:
    date, argent_dispo, argent_mois = infos
    argent_dispo = float(argent_dispo)
    argent_debut_mois = float(argent_mois)

    print("Date et heure de la dernière ligne :", date)
    print("Argent disponible:", argent_dispo)
    print("Argent au début du mois:", argent_mois)
else:
    print("Le fichier CSV est vide.")

