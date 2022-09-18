import random
import os
import discord

bot = discord.Client()


@bot.event
async def on_ready():
    print('Granowicki Bot is online')


@bot.event
async def on_message(message):
    # Sprawdzanie czy wiadomość nie została wysłana przez bota, jeśli była - nic nie robić
    if message.author == bot.user:
        return

    # Tabela ID na których spingowanie bot ma zareagować
    list = [f'<@!{346706048616497152}>', f'<@!{624618386378457109}>', f'<@!{296733345914683396}>',
            f'<@!{583348312636260362}>']

    # Tabela z pseudonimami Kacpra J
    pseudonimy = ['man1', 'man2']

    # Lista tekstów którymi bot ma reagować na wiadomości grubasa
    tekst = ['placeholder1', 'placeholder2']

    # Tabela z emoji
    emoji = ['https://cdn.discordapp.com/emojis/790214962516590632.png?v=1',
             'https://cdn.discordapp.com/emojis/806860649883500544.png?v=1',
             'https://cdn.discordapp.com/emojis/824236443437498408.png?v=1']

    # Odpowiadanie na nazwanie Kacpra J
    for i in pseudonimy:
        if i in message.content:
            await message.channel.send(random.choice(emoji))

    # Jeśli Kotleciok coś napisze, wylosuj jeden tekst z listy i wyślij
    if (message.author.id == '265855940157243392' or message.author.id == '410136254458494976' in message.content):
        if (random.randint() % 3 == 0):
            await message.channel.send(random.choice(tekst))

    # Na hasło wylosuj jeden tekst z listy i wyślij
    if ('Daj głos' in message.content):
        await message.channel.send(random.choice(tekst))

    # Jeśli ktoś z listy zostanie spingowany - odpowiedz
    if message.content in list:
        await message.channel.send("Po chuj pingujesz " + message.author.mention + "?")

    # Wysyłanie memika gdy godzik spinguje irego i napisz 2LO
    if message.author.id == 624618386378457109 and f'<@!{410136254458494976}>' in message.content and '2LO' in message.content:
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/751861351378583562/835884289705902100/unknown.png')

    # Jeśli ktoś szuka kogoś do grania w szachy, napisz
    if 'chess' in message.content or 'szachy' in message.content:
        await message.channel.send(message.author.name + " szuka kogoś do gry!")

    muzyczka = bot.get_channel(751862595220275275)


# Ale komentarze profesjonalne
bot.run(os.getenv('Granowice'))