import discord
import os
import datetime
import discord.ext.commands


client = discord.ext.commands.Bot('$')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author)
    if str(message.author) == "GitHub#0000":
        print(message.embeds[0].title)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$reload'):
        print("reloading Voting")
        client.reload_extension('Voting')

client.load_extension('Voting')
client.run(os.getenv('discord_bot'))
