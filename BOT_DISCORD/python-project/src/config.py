"""
Configuration du Bot Discord
Ce fichier contient toutes les constantes et configurations nécessaires au bot:
- ID de l'utilisateur autorisé
- Sources d'événements tech
- Liste des événements majeurs
- Configuration des permissions Discord (intents)
"""

import discord

# ID Discord de l'administrateur du bot qui peut gérer les invitations
# Remplacer VOTRE_ID_DISCORD par votre vrai ID Discord
# Pour obtenir votre ID: Activer le mode développeur dans Discord
# Clic droit sur votre nom -> Copier l'identifiant
AUTHORIZED_USER_ID = solairefullautiste  # Mettez votre vrai ID ici

# Liste des sites sources pour la recherche d'événements tech
EVENT_SOURCES = [
    "https://www.meetup.com/",
    "https://www.eventbrite.com/",
    "https://www.welcometothejungle.com/"
]

# Liste des événements majeurs tech en France à surveiller
MAJOR_EVENTS = [
    "Paris Web",
    "Devoxx France",
    "Web2Day (Nantes)",
    "MiXiT (Lyon)",
    "BlendWebMix (Lyon)",
    "DevFest (plusieurs villes)",
    "Tech&Fest"
]

def setup_intents():
    """Configure et retourne les permissions nécessaires pour le bot"""
    intents = discord.Intents.default()
    intents.messages = True      # Permission de lire les messages
    intents.guilds = True        # Permission d'interagir avec les serveurs
    intents.dm_messages = True   # Permission pour les messages privés
    intents.message_content = True  # Permission de lire le contenu des messages
    return intents
