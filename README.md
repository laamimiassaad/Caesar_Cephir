# Caesar Cipher

Un petit script Python interactif pour chiffrer et déchiffrer du texte avec un chiffrement de César.

## Aperçu

Le programme décale chaque lettre de l'alphabet d'un nombre de positions donné.
Il conserve les majuscules, les minuscules et laisse les caractères spéciaux inchangés.

## Fonctionnalités

- Chiffrement du texte avec un décalage vers l'avant
- Déchiffrement du texte avec un décalage vers l'arrière
- Conservation des lettres majuscules et minuscules
- Conservation des espaces, chiffres et caractères spéciaux

## Prérequis

- Python 3

## Lancer le script

Depuis le dossier du projet, exécutez :

```bash
python Caesar_Cipher.py
```

## Utilisation

Au lancement, le script demande successivement :

1. `encrypt` pour chiffrer ou `decrypt` pour déchiffrer
2. Le texte à traiter
3. Une valeur de décalage entre `1` et `25`

Exemple :

- Mode : `encrypt`
- Texte : `Hello World`
- Décalage : `3`

Résultat :

```text
Encrypted text: Khoor Zruog
```

## Règles de saisie

- Le décalage doit être un entier compris entre `1` et `25`
- Toute valeur différente de `encrypt` ou `decrypt` affiche un message d'erreur
- Le programme s'exécute dans le terminal et attend des saisies utilisateur

## Structure du projet

- [Caesar_Cipher.py](Caesar_Cipher.py) : logique principale du chiffrement et du déchiffrement
- [README.md](README.md) : documentation du projet

## Améliorations possibles

- Ajouter une boucle pour traiter plusieurs textes sans relancer le script
- Gérer des entrées plus robustes pour éviter les erreurs de conversion
- Proposer une interface graphique ou une version web légère
