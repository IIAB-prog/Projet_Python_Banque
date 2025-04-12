# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 19:44:01 2025

@author: IIAB_
"""
from datetime import datetime  # Import de datetime

# Création de la classe banque
class Banque:
    # Initialisation
    def __init__(self, nom_banque, type_compte):
        self.nom_banque = nom_banque
        self.siege = "Ouagadougou"
        self.type_compte = type_compte

# Création de la classe Client qui hérite la classe Banque
class Client(Banque):
    # Initialisation
    def __init__(self, nom_banque, type_compte, nom, prenom, age, adresse, telephone, solde):
        super().__init__(nom_banque, type_compte)
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.telephone = telephone
        self.solde = solde
        self.type_client = self.definir_type_client()
    
    # Fonction pour définir le type de client
    def definir_type_client(self):
        if self.solde >= 100000000:
            return "VIP"
        elif self.solde >= 10000000:
            return "Classique"
        elif self.solde >= 100000:
            return "Jeune Étudiant"
        else:
            return "Non défini"

    # Fonction pour enregistrer les transaction dans un fichier rapport.txt
    def enregistrer_transaction(self, type_transaction, montant):
        # Ajout de la date et de l'heure actuelles
        date_heure_actuelle = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Format de la date
        # Création ou ouverture du fichier rapport.txt
        with open("rapport.txt", "a") as fichier:
            #Ecriture dans le fichier
            fichier.write(f"Client :{self.nom} {self.prenom} - Téléphone: {self.telephone} - Type de transaction: {type_transaction} - Montant: {montant} - Solde actuel: {self.solde} - Date : {date_heure_actuelle}  \n")

    # Fonction pour effectuer un dépôt sur le compte d'un tiers
    def Depot(self, montant):
        if montant > 0:  # Vérification d'un montant positif
            self.solde += montant  # Processus de dépôt
            self.enregistrer_transaction("Dépot", montant)# Enregistrement du dépôt dans le rapport
            print(f"Dépôt effectué : {montant}. Nouveau solde : {self.solde}")
        

    # Fonction pour effectuer un retrait sur le compte d'un tiers
    def Retrait(self, montant):
        if  montant <= self.solde:  # Vérification d'un montant positif et solde du compte
            self.solde -= montant  # Processus de retrait
            self.enregistrer_transaction("Retrait", montant)  #Enregistrement du retrait dans le rapport
            print(f"Retrait effectué : {montant}. Nouveau solde : {self.solde}")
        else:
            print("Montant invalide ou solde insuffisant.")
            
    # Fonction pour le solde du compte d'un tiers
    def Afficher_Solde(self):
        print(f"Le solde de votre compte est : {self.solde}")

