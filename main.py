import os
import discord
from src.discordBot import DiscordClient, Sender
from src.logger import logger
import google.generativeai as palm
from src.server import keep_alive

# Set up the PaLM API
palm.configure(api_key = "BARD_API_KEY")
model = palm.Model(output_token_limit=500)

def chat_completion(message: str) -> str:
# Get the PaLM API response
    response = palm.chat(messages=message, candidate_count = 0)
    output = response.messages[1]
    return output['content']

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
        # Truncate the length of the message to 2000 characters, but set this to 2000 chars would still cause this problem. so I set it to 1900.
        #if len(receive) > 1900:
        #    receive = receive[:1900]
        await sender.send_message(interaction, message, receive)


    client.run("DISCORD_TOKEN")


if __name__ == '__main__':
    keep_alive()
    run()
