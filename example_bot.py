
import discord

intents = discord.Intents.default()
TOKEN = 'MTAyMTQ5MjQzOTUxODgwNjE1NA.GRs6LH.rM3B-RQiCfXE3Tlm08yHsUE5IONYkqVCiaYuPo'

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)