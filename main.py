import os
import discord
from src.discordBot import DiscordClient, Sender
from src.logger import logger
import google.generativeai as palm
from src.server import keep_alive

# Set up the PaLM API
palm.configure(api_key = "PaLM_API_KEY")
model = palm.types.Model(
    name = "models/chat-bison-001",
    base_model_id= "chat-bison",
    version= "001",
    display_name= "the Bison",
    description= "the PaLM Bison",
    input_token_limit= 145,
    output_token_limit= 145,
    supported_generation_methods= ["generateMessage"],
)

def chat_completion(message: str) -> str:
# Get the PaLM API response
    response = palm.chat(messages=message, candidate_count = 0)
    output = response.messages[1]
    return output['content']

def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="palm", description="Have a chat with PaLM Bison")
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
