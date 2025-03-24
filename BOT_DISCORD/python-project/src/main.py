"""
Point d'entrée principal du Bot Discord
Ce fichier contient:
- L'initialisation du bot
- La gestion des événements Discord (messages, rejoindre un serveur, etc.)
- Les commandes du bot
- La logique de gestion des canaux actifs
"""

import discord
from discord.ext import commands
from config import setup_intents, AUTHORIZED_USER_ID, EVENT_SOURCES, MAJOR_EVENTS
from services.event_service import EventNotifier

# Initialisation du bot avec les permissions nécessaires
bot = commands.Bot(command_prefix="!", intents=setup_intents())
event_notifier = None

async def fetch_tech_events():
    # Placeholder for actual scraping or API calls to fetch events
    return [
        {"name": "Devoxx France", "date": "2023-11-15", "location": "Paris"},
        {"name": "Web2Day", "date": "2023-12-01", "location": "Nantes"}
    ]

@bot.event
async def on_ready():
    """Appelé quand le bot est connecté et prêt"""
    print(f"Logged in as {bot.user}")
    global event_notifier
    event_notifier = EventNotifier(bot)
    bot.loop.create_task(event_notifier.notify_tech_events())

@bot.event
async def on_message(message):
    """
    Gère les messages reçus par le bot
    - Messages privés pour les invitations
    - Sélection du canal actif
    - Réactions aux salutations
    """
    if message.author == bot.user:
        return

    # Gestion des invitations par message privé
    if isinstance(message.channel, discord.DMChannel) and message.author.id == AUTHORIZED_USER_ID:
        if "discord.gg/" in message.content:
            invite_link = message.content.strip()
            try:
                invite = await bot.fetch_invite(invite_link)
                await invite.accept()
                await message.channel.send("J'ai rejoint le serveur avec succès !")
            except Exception as e:
                await message.channel.send(f"Erreur lors de la tentative de rejoindre le serveur : {e}")
        return

    # Gestion de la sélection du canal
    if message.guild and message.channel.name == "general" and bot.user in message.mentions:
        if message.channel_mentions:
            selected_channel = message.channel_mentions[0]
            event_notifier.active_channels[message.guild.id] = selected_channel.id
            await message.channel.send(
                f"Je serai désormais actif uniquement dans le salon {selected_channel.mention}."
            )
        else:
            await message.channel.send("Veuillez mentionner un salon textuel valide.")
        return

    # Gestion des messages dans les serveurs
    if message.guild:
        guild_id = message.guild.id
        if guild_id in event_notifier.active_channels and message.channel.id == event_notifier.active_channels[guild_id]:
            if any(greeting in message.content.lower() for greeting in ["bonjour", "salut", "hey", "hello", "yo"]):
                await message.add_reaction("👋")

@bot.event
async def on_guild_join(guild):
    """
    Appelé quand le bot rejoint un nouveau serveur
    Demande dans quel canal il doit être actif
    """
    general_channel = discord.utils.get(guild.text_channels, name="general")
    if general_channel:
        await general_channel.send(
            "Dans quel salon textuel souhaitez-vous que je reste actif ? Veuillez mentionner le salon."
        )

@bot.command()
async def test(ctx):
    """Commande de test pour vérifier que le bot fonctionne"""
    await ctx.send("Je suis en ligne et fonctionnel ! 👋")

if __name__ == "__main__":
    # Démarrage du bot
    print("Welcome to the Python Project!")
    with open("../../bot_token.txt", "r") as token_file:
        bot_token = token_file.read().strip()
    bot.run(bot_token)