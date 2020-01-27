from discord.ext import commands
import datetime


class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        result = "author: {}. Created at: {}. Deleted at : {}. \n ```{}```".format(message.author,
                message.created_at, datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"), message.system_content)
        for channel in message.guild.channels:
            if channel.name == "mod-logs":
                await channel.send(result)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        result = f"The message by: {before.author},```{before.system_content}``` was changed to ```{after.system_content}``` on, {datetime.datetime.now().strftime('%I:%M%p on %B %d, %Y')}"

        for channel in after.guild.channels:
            if channel.name == "mod-logs":
                await channel.send(result)


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        message = f"The user: {user.system_content} was banned on {datetime.datetime.now().strftime('%I:%M%p on %B %d, %Y')}"

        for channel in message.guild.channels:
            if channel.name == "mod-logs":
                await channel.send(message)


class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.l()
    async def on_member_unban(self, guild, user):
        message = f"The user: {user.system_content} was unbanned on {datetime.datetime.now().strftime('%I:%M%p on %B %d, %Y')}"

        for channel in message.guild.channels:
            if channel.name == "mod-logs":
                await channel.send(message)


def setup(bot):
    bot.add_cog(Logging(bot))
    bot.add_cog(Ban(bot))
    bot.add_cog(Unban(bot))



