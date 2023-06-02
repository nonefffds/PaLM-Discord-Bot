import os

from src.discordBot import DiscordClient, Sender
from src.logger import logger
#from src.models import BardModel
import google.generativeai as palm
from src.server import keep_alive


palm.configure(api_key = "BARD_API_KEY")

def chat_completion(self, message) -> str:
# Get the PaLM API response
    response = palm.chat(messages=message, candidate_count = 0)
    output = response.messages[1]
    print (output['content'])

def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="bard", description="Have a chat with Bard")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        receive = chat_completion(message)
        await sender.send_message(interaction, message, receive)


    client.run("DISCORD_TOKEN")


if __name__ == '__main__':
    keep_alive()
    run()
