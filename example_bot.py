import discord
import token_decoder

#Idk
intents = discord.Intents.default()
client = discord.Client(intents=intents)

#Decoding the token
decoder = token_decoder.Tokener()
token = decoder.accessFile(decoder)


#Launching bot
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)