import os

from src.discordBot import DiscordClient, Sender
from src.logger import logger
from src.models import BardModel
from src.server import keep_alive


models = BardModel(api_key= "PaLM_API_KEY")


def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="bard", description="Have a chat with Bard")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        receive = models.chat_completion(message)
        await sender.send_message(interaction, message, receive)


    client.run("DISCORD_TOKEN")


if __name__ == '__main__':
    keep_alive()
    run()
