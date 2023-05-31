import os

import discord

from src.discordBot import DiscordClient, Sender
from src.logger import logger
from src.bard import Bard
from src.models import BardModel
from src.memory import Memory
from src.server import keep_alive


models = BardModel(api_key= "OPENAI_API")
memory = Memory(system_message= "SYSTEM_MESSAGE")
bard = Bard(models, memory)


def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="chat", description="Have a chat with Bard")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        receive = bard.get_response(user_id, message)
        await sender.send_message(interaction, message, receive)

    @client.tree.command(name="reset", description="Reset Bard conversation history")
    async def reset(interaction: discord.Interaction):
        user_id = interaction.user.id
        logger.info(f"resetting memory from {user_id}")
        try:
            bard.clean_history(user_id)
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(f'> Reset Bard conversation history < - <@{user_id}>')
        except Exception as e:
            logger.error(f"Error resetting memory: {e}")
            await interaction.followup.send('> Oops! Something went wrong. <')

    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    keep_alive()
    run()
