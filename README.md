# POO_Projet
## Langage 
Python 3.8.6

## Auteurs  
- Name : FrigoFri
- Ferekh Khaled : 17341
- Thierry Joel Tchanteu Moumi : 17367

# Installation
- Télecharger ou clone le dossier POO_Projet de github en tapant :
    git clone https://github.com/17341/POO_Projet
- Installer Python 3 et Pandas sur votre pc si ce n'est pas déja fait

# How to test 
- Ouvrer le dossier POO_Projet dans un terminal:
    - Taper : python main_controle.py

# Informations Simulateur 

## A quoi ça peut servir?  
- Simuler des tests dans un réseau électrique pour des chercheurs
- Créer et surveiller un ou plusieurs réseau(x) électrique

## Fonctionnalités
- Création de(s) réseau(x) électrique complet(es)(centrales,consommateurs,distributeur,dissipateur,stock,noeuds,lignes,...)
- Possibilité d'ajouter et de supprimer des élements dans le(s) réseau(x)
- Mettre à jour et afficher les productions, frais de productions, émissions de CO2 des centrales ,consommations et prix de consommations, puissances de lignes/noeuds, status des élements, ...
- Envoyer des messages d'erreurs, d'alertes, modifications de produciotn/consommation, arrêt/marche centrales, ...
- Implementation d'un sytème de marché pour achat/vente d'électricité/combustible à l'étranger automatiquement 
- Implementation d'un sytème de méteo pour controler automatiquement les centrales solaires et les parcs éoliennes
- Implementation d'un sytème de stock pour stocker le surplus de productions, si pas de place en stock on vend à l'etranger
- Controle automatique des lignes et noeuds pour eviter les problèmes de puissances

## Important
- Les differents valeurs utilisées dans le test sont à titre indicatif, on utilise le module random pour les productions, consommations, prix du marchés, méteos
- Vous pourrez donc avoir des valeurs irréalistes et qui vous paraissent illogiques, ce n'est finalement qu'une simulation de test
- Pour l'instant : si vous voulez changer/ajouter des élements/valeurs, ceci ce fait dand le main_controle

## A ajouter
- Une nouvelle version sera ajouter plus-tard pour vous permettre : 
    - Modifier dynamiquement les élements du réseau en même temps que les mises à jour
    - Option de simuler les données d'une base de données
    - Une interface graphique