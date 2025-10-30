# Modèle de Partage de Rente Minière

**Membres du groupe :**
* Rilwanou Mahaman Lawal
* Madou Gagi Ismaël
* Mohamed ZEBA
* Mohamed ZEBA

**Tuteur :** Jules MAES
**Université :** UNIVERSITÉ DE REIMS CHAMPAGNE-ARDENNE

---

## 🎯 Objectif du Projet

[cite_start]Ce projet vise à développer un outil d'aide à la décision [cite: 99] pour modéliser et simuler le partage de la rente minière entre un État hôte et des investisseurs étrangers. [cite_start]L'objectif est de fournir aux décideurs publics (administrations fiscales) un moyen d'évaluer différents scénarios fiscaux lors des négociations de contrats miniers [cite: 100][cite_start], afin d'assurer un partenariat "gagnant-gagnant"[cite: 33].

[cite_start]L'outil, développé en **Python** [cite: 105][cite_start], s'appuie sur un cas d'étude concret : la mine d'or de **Houndé au Burkina Faso**[cite: 98].

## 🗃️ Structure du Projet

* `/data` : Contient les données brutes (fichiers CSV) :
    * [cite_start]`donnees_mine_hounde.csv` : Données de production, CAPEX et OPEX[cite: 117].
    * [cite_start]`donnees_amortissement.csv` : Détails des plans d'amortissement[cite: 118, 119].
    * [cite_start]`donnees_fiscales_bf.csv` : Données fiscales issues du Code minier de 2003[cite: 121].
* `/src` : Contient le code source du modèle de simulation en Python.
* `/notebooks` : Carnets Jupyter pour l'analyse exploratoire et la visualisation.
* [cite_start]`/rapport` : Contient les rapports d'étapes et la documentation du projet (comme le "Rapport d'étapes _IVE.pdf" [cite: 1-116]).

## 📈 Contexte

[cite_start]Les pays africains riches en ressources font face au défi de capter une part équitable de la richesse générée[cite: 12]. [cite_start]Historiquement, des contrats déséquilibrés [cite: 48] [cite_start]et une faible capacité à modéliser les revenus [cite: 32] [cite_start]ont contribué à la "malédiction des ressources"[cite: 15, 51]. Ce projet cherche à fournir un outil pratique pour remédier à ce problème.

## 🚀 Utilisation (À compléter)

1.  Clonez le dépôt :
    ```bash
    git clone [https://github.com/VOTRE-NOM/RentShare-Simulator.git](https://github.com/VOTRE-NOM/RentShare-Simulator.git)
    ```
2.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
3.  Exécutez le modèle (exemple) :
    ```bash
    python src/main.py
    ```