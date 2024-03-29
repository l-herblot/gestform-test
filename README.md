# Aspects fonctionnels

## Énoncé
Soit une liste aléatoire de nombres entiers, compris entre -1000 et 1000. Pour chaque nombre n de liste, on veut effectuer les opérations suivantes:
- si le nombre est divisible par 3 : on affiche Geste
- si le nombre est divisible par 5 : on affiche Forme
- si le nombre est divisible par 3 et par 5 : on affiche Gestform (d’où le nom du test)
- sinon : on affiche le nombre n

## Compréhension
Il est possible d'interpréter l'énoncé de deux façons :
- Affichage exclusif : le programme n'affiche qu'un seul "mot" pour chaque nombre traité (par exemple "Geste" pour un nombre divisible par 3 et "Gestform" pour un nombre à la fois divisible par 3 et 5)
- Affichage exhaustif : le programme peut afficher plusieurs "mots" pour chaque nombre traité (par exemple "Geste" pour un nombre divisible par 3 et "Geste", "Forme" et "Gestform" pour un nombre à la fois divisible par 3 et 5)

Etant donnée que la compréhension la plus commune est la première, et afin de respecter le principe de moindre surprise (clean code), c'est cette approche qui est retenue ici.

Bien entendu, dans un cas plus concret, si une demande fonctionnelle était ambigüe il serait nécessaire de questionner un expert métier (Product Owner ou autre) pour s'assurer de l'implémentation à mettre en place.

# Aspects techniques
## Installation des dépendances
```pip install -r requirements. txt```

## Formatage du code
```black .```

## Exécution des tests unitaires
```pytest```

## Automatisation du process
Un workflow github a été mis en place pour s'assurer du bon formatage du code et de la validation des tests de façon automatisée.
