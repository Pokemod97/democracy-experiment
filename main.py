import discord
import os
import datetime
import discord.ext.commands


class CustomBot(discord.ext.commands.Bot):

    def reload(self):
        self.reload_extension("Voting")


client = CustomBot("$")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.load_extension('Voting')
client.run(os.getenv('discord_bot'))
