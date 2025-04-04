# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 19:51:34 2025

@author: IIAB_
"""

from gestion import Client

if __name__ == "__main__":
     # Création d'un client avec des informations de base
     client1 = Client(
     nom_banque="Coris Banque International",
     siege="Ouagadougou",
     type_compte="Courant",
     nom="IMA",
     prenom="ADAM",
     age=27,
     adresse="Avenue Kwame nkrumah",
     solde=150000000
     )

     # Affichage des informations du client
     print(f"Nom du client : {client1.nom} {client1.prenom}")
     print(f"Type de client : {client1.type_client}")
     print(f"Adresse : {client1.adresse}")
     print(f"Solde initial : {client1.solde}")
     # Dépôt d'argent
     client1.Depot(50000)
     # Retrait d'argent
     client1.Retrait(10000)
     # Affichage du solde final
     client1.Afficher_Solde()