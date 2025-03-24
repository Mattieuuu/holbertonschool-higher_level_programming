# Bot Discord Python

## 📝 Description
Un bot Discord simple développé en Python 

Je vais t'expliquer la structure standard d'un projet de bot Discord en Python :

```
python-project/
├── src/                      # Dossier principal du code source
│   ├── main.py              # Point d'entrée principal du bot
│   ├── controllers/         # Gestion de la logique des commandes
│   │   └── __init__.py     
│   ├── models/             # Définition des structures de données
│   │   └── __init__.py
│   ├── utils/              # Fonctions utilitaires réutilisables
│   │   └── __init__.py
│   └── tests/             # Tests unitaires et d'intégration
│       ├── __init__.py
│       └── test_main.py
├── requirements.txt       # Liste des dépendances Python
└── README.md            # Documentation du projet
```

Détails de chaque dossier :

- **src/** : Contient tout le code source de l'application
  - **controllers/** : Contient la logique des commandes du bot
  - **models/** : Pour définir les structures de données ou les classes
  - **utils/** : Pour les fonctions helper et utilitaires
  - **tests/** : Pour tous les tests de l'application

- **requirements.txt** : Liste toutes les bibliothèques Python nécessaires
- **README.md** : Documentation expliquant comment installer et utiliser le bot

Les fichiers `__init__.py` sont des fichiers Python vides qui indiquent que le dossier est un package Python.

## 🚀 Installation

1. Clonez le repository :
```bash
git clone <votre-repo-url>
cd python-project
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Créez un fichier `bot_token.txt` à la racine du projet et ajoutez votre token Discord.

## ⚙️ Configuration requise
- Python 3.8 ou supérieur
- discord.py

## 🛠️ Fonctionnalités
- Réagit avec 👋 aux messages contenant "bonjour", "salut", "hey", "hello", "yo"
- Préfixe des commandes : `!`

## 🔧 Utilisation
Pour lancer le bot :
```bash
python src/main.py
```

## 📋 Liste des commandes
- En cours de développement...

## 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou un pull request.

## 📝 License
MIT License