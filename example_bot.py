import discord
import token_decoder

intents = discord.Intents.default()
client = discord.Client(intents=intents)

#Decoding the token
decoder = token_decoder.Tokener()
token = decoder.accessFile(decoder)

#TestID 1021492127647154208
#GoodId 751861351378583562
channelId = int(751861351378583562)



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #Saving channel and server for something
    channel = client.get_channel(int(channelId))
    guild = channel.guild
    counter = 0
    #If the message is not empty, print it into console with it's author
    async for message in channel.history(limit = 2147483647, oldest_first = True):
        if message.content != '':
            #Change this to save into database
            print(str(message.author))
            print(str(message.content) + '\n######################')
            counter +=1
            print(counter)

if __name__ == "__main__":
    client.run(token)