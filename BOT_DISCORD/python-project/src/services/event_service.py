"""
Service de gestion des événements tech
Ce module gère:
- La récupération des événements tech (actuellement mockée)
- La notification des événements dans les canaux Discord configurés
- Le stockage des canaux actifs par serveur
"""

import asyncio
from typing import List, Dict

async def fetch_tech_events() -> List[Dict[str, str]]:
    """
    Récupère la liste des événements tech à venir
    Actuellement utilise des données statiques, à remplacer par du scraping réel
    Returns:
        List[Dict]: Liste des événements avec nom, date et lieu
    """
    # TODO: Implémenter le vrai scraping des événements
    return [
        {"name": "Devoxx France", "date": "2023-11-15", "location": "Paris"},
        {"name": "Web2Day", "date": "2023-12-01", "location": "Nantes"}
    ]

class EventNotifier:
    """
    Gère la notification des événements tech dans les canaux Discord configurés
    """
    
    def __init__(self, bot):
        """
        Initialise le notificateur avec une référence au bot Discord
        Args:
            bot: Instance du bot Discord
        """
        self.bot = bot
        self.active_channels = {}  # Stocke les associations {guild_id: channel_id}

    async def notify_tech_events(self):
        """
        Boucle infinie qui notifie périodiquement les événements tech
        dans tous les canaux configurés
        """
        while True:
            print("Fetching upcoming tech events...")
            events = await fetch_tech_events()
            for guild_id, channel_id in self.active_channels.items():
                channel = self.bot.get_channel(channel_id)
                if channel:
                    message = "Voici les prochains événements tech et informatiques en France :\n"
                    for event in events:
                        message += f"- **{event['name']}** le {event['date']} à {event['location']}\n"
                    await channel.send(message)
            await asyncio.sleep(60)  # Attente d'une minute entre chaque notification
