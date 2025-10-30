# Modèle de Partage de Rente Minière

**Membres du groupe :**
* Rilwanou Mahaman Lawal
* Madou Gagi Ismaël
* Mohamed ZEBA
* Cheikh LO

**Tuteur :** Jules MAES
**Université :** UNIVERSITÉ DE REIMS CHAMPAGNE-ARDENNE

---

## 🎯 Objectif du Projet

Ce projet vise à développer un outil d'aide à la décision [cite: 99] pour modéliser et simuler le partage de la rente minière entre un État hôte et des investisseurs étrangers.L'objectif est de fournir aux décideurs publics (administrations fiscales) un moyen d'évaluer différents scénarios fiscaux lors des négociations de contrats miniers, afin d'assurer un partenariat "gagnant-gagnant"[cite: 33].

L'outil, développé en **Python**, s'appuie sur un cas d'étude concret : la mine d'or de **Houndé au Burkina Faso**.

## 🗃️ Structure du Projet

* `/data` : Contient les données brutes (fichiers CSV) :
    * `donnees_mine_hounde.csv` : Données de production, CAPEX et OPEX.
    * `donnees_amortissement.csv` : Détails des plans d'amortissement.
    * `donnees_fiscales_bf.csv` : Données fiscales issues du Code minier de 2003.
* `/src` : Contient le code source du modèle de simulation en Python.
* `/notebooks` : Carnets Jupyter pour l'analyse exploratoire et la visualisation.
* `/rapport` : Contient les rapports d'étapes et la documentation du projet (comme le "Rapport d'étapes _IVE.pdf") .

## 📈 Contexte

Les pays africains riches en ressources font face au défi de capter une part équitable de la richesse générée. Historiquement, des contrats déséquilibrés  et une faible capacité à modéliser les revenus ont contribué à la "malédiction des ressources". Ce projet cherche à fournir un outil pratique pour remédier à ce problème.

## 🚀 Utilisation (À compléter)

1.  Clonez le dépôt :
2.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
3.  Exécutez l'interface de calcul :
    ```bash
    streamlit run src/interface.py
    ```