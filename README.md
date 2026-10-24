Projet Data Analytics — E-commerce

Analyse de données e-commerce avec SQL, Python, Pandas et Matplotlib

1. Présentation du projet

Objectif

Ce projet consiste à analyser les données d'une plateforme e-commerce afin d'identifier les tendances commerciales, de suivre les indicateurs clés de performance (KPI) et de transformer les données en informations utiles à la prise de décision.

Le projet comprend l'exploration des données, leur manipulation avec Pandas, la visualisation avec Matplotlib et la présentation des résultats métier.

Important : les données utilisées sont synthétiques et destinées à l'apprentissage et à la démonstration de compétences en Data Analytics. Elles ne représentent pas des transactions réelles.

2. Questions métier

L'analyse vise à répondre aux questions suivantes :

Quel est le chiffre d'affaires par année et par mois ?

Comment le chiffre d'affaires évolue-t-il au fil du temps ?

Quelle est la répartition des commandes selon leur statut ?

Quelles régions génèrent le plus de chiffre d'affaires ?

Quel est le nombre de commandes par région ?

Quel est le montant moyen d'une commande ?

Quel est le taux d'annulation des commandes ?

Quels enseignements peuvent aider à améliorer la performance commerciale ?

3. Indicateurs clés de performance (KPI)

Les principaux indicateurs étudiés sont :

Chiffre d'affaires (CA) : montant total généré par les commandes retenues dans l'analyse.

Nombre de commandes : volume total de commandes.

Panier moyen : montant moyen d'une commande.

Taux d'annulation : proportion des commandes annulées parmi l'ensemble des commandes.

Évolution du chiffre d'affaires : suivi mensuel et annuel.

Chiffre d'affaires par région : comparaison des performances géographiques.

Répartition des commandes par statut : analyse des commandes selon leur état.

4. Outils et technologies

SQL / MariaDB : extraction et interrogation des données.

Python : traitement et analyse des données.

Pandas : nettoyage, manipulation et agrégation des données.

Matplotlib : création de graphiques.

Jupyter Notebook : exploration et documentation des analyses.

Git / GitHub : versionnement et publication du projet.

5. Structure du projet


ecommerce_data_analytics/
├── notebooks/
│   └── 01_data_exploration.ipynb
├── reports/
│   ├── graphiques/
│   └── rapport_analyse_ecommerce.pdf
├── src/
│   └── database.py
├── sql/
├── data/
├── .env.example
├── .gitignore
└── README.md


Les données brutes, les identifiants de connexion et les fichiers de configuration privés ne doivent pas être publiés sur GitHub.

6. Premiers résultats

L'analyse exploratoire porte sur un jeu de données synthétiques comprenant 200 000 commandes.

Indicateur

Résultat

Nombre total de commandes

200 000

Commandes annulées

10 115

Taux d'annulation

5,06 %

Panier moyen global

26 907,96 DH

Chiffre d'affaires hors commandes annulées

5 109 417 459,57 DH

Ces résultats décrivent uniquement le jeu de données d'entraînement. Le chiffre d'affaires hors commandes annulées est calculé en excluant les commandes dont le statut est cancelled.

7. Livrables

Le dépôt contient les éléments suivants :

Un notebook d'exploration et d'analyse des données.

Des graphiques réalisés avec Matplotlib.

Un rapport d'analyse au format PDF.

Un script Python pour tester la connexion à la base de données.

8. Installation et exécution

Pour reproduire le projet :

Cloner le dépôt GitHub.

Activer l'environnement Python et installer les dépendances nécessaires.

Créer un fichier .env local à partir de .env.example.

Configurer la connexion à une base de données MariaDB compatible.

Exécuter le script de connexion.

Ouvrir le notebook dans Jupyter Notebook ou VS Code.

Exécuter les cellules du notebook pour reproduire les analyses.

Sécurité : ne jamais publier le fichier .env, les mots de passe ou les identifiants de connexion.

9. Perspectives d'amélioration

Les prochaines étapes du projet pourront inclure :

L'approfondissement de l'analyse temporelle du chiffre d'affaires.

L'identification des régions les plus performantes.

L'analyse du comportement des clients.

L'étude des facteurs associés aux annulations.

La création d'un tableau de bord interactif.

L'amélioration des recommandations métier à partir des résultats.

Auteur

Asmae Elhaddouchi
Portfolio Junior Data Analyst

Consulter mon profil GitHub
