import discord
import os
from dotenv import load_dotenv
from gpt import ChatGPT


load_dotenv() 

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

chatGPT = ChatGPT()
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content:
        response = chatGPT.getOpenAIResponse(message.content)
        await message.channel.send(response)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") 

client.run(DISCORD_TOKEN)