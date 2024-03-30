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
        print(derniere_info.split(","))
        return derniere_info.split(",")

# Lire le fichier CSV et récupérer la dernière ligne
infos_data = get_last_row("stats.csv")
date, argent_dispo, argent_mois = infos_data
date_actuelle = datetime.datetime.now().strftime("%H:%M:%S|%Y-%m")
def afficher_infos(infos_data, date, argent_dispo, argent_mois):
    if infos_data:
        argent_dispo = float(argent_dispo)
        argent_mois = float(argent_mois)

        print("Date et heure de la dernière ligne :", date)
        print("Argent disponible:", argent_dispo)
        print("Argent au début du mois:", argent_mois)
    else:
        print("Le fichier CSV est vide.")
        
afficher_infos(infos_data, date, argent_dispo, argent_mois)

def ajouter_ligne_dernier_minute(csv_file, date_actuelle, argent_restant, argent_mois):
    with open(csv_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow("\n")
        writer.writerow([date_actuelle, argent_restant, argent_mois])
        
ajouter_ligne_dernier_minute("stats.csv", date_actuelle, argent_dispo, argent_mois)

