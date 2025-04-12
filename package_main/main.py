# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 19:51:34 2025

@author: IIAB_
"""

import sys
sys.path.insert(0, 'D:\MASTER_IA\Python Data science\TP_DEV') #0 indique la position dans le path
from package_gestion.gestion import Client

# Fonction pour saisir le solde du client
def saisir_solde():
    while True:
        try:
            solde = float(input("Entrez le solde : "))
            if solde < 0:
                print("Le solde ne peut pas être négatif.")
            else:
                return solde
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Fonction pour saisir le numéro telephone  du client
def saisir_telephone():
    while True:
        telephone = input("Entrez le numéro de téléphone : ")
        if telephone.isdigit() and len(telephone) == 8:
            return telephone
        else:
            print("Veuillez entrer un numéro de téléphone valide (6 chiffres exactement)).")



if __name__ == "__main__":

    liste_client = []
    
    print("\n|*************************************************************|\n")
    print("|***************Création des comptes clients******************|")
    print("\n|*************************************************************|\n")
    for i in range(2):
        print(f"\nInformations du client {i+1} :")
        
        nom_banque = input("Nom de la banque : ")
        siege=input("Siege de la Banque: ")
        type_compte = input("Type de compte : ")
        
        nom = input("Nom du client : ")
        prenom = input("Prénom du client : ")
        age = int(input("Âge du client : "))
        adresse = input("Adresse du client : ")
        
        telephone = saisir_telephone()
        solde = saisir_solde()

        client = Client(nom_banque, siege, type_compte, nom, prenom, age, adresse, telephone, solde)
        liste_client.append(client)

    print("\n|*************************************************************|\n")
    print("|***************Opération sur les comptes clients*************|")
    print("\n|*************************************************************|\n")
    # Afficher les informations des clients
    for i, client in enumerate(liste_client):
        print(f"\nClient {i+1} :")
        print(f"Nom : {client.nom} {client.prenom}")
        print(f"Adresse : {client.adresse}")
        print(f"Téléphone : {client.telephone}")
        print(f"Solde initial: {client.solde}")
        print(f"Type de client : {client.type_client}")
        # Dépôt d'argent
        print("\n---------------Dépot d'argent----------------")
        client.Depot(saisir_solde())
        # Retrait d'argent
        print("\n---------------Retrait d'argent--------------")
        client.Retrait(saisir_solde())
        # Affichage du solde final
        print("\n---------------Solde Final----------------")
        client.Afficher_Solde()
