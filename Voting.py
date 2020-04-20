from discord.ext import commands, tasks
from github import Github
import os


class Voting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.g = Github(os.getenv("github_token"))
        self.repo = self.g.get_repo("Pokemod97/democracy-experiment")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print("reaction added")
        print(reaction.count)
        member_count = len(reaction.message.guild.members)
        for role in reaction.message.guild.roles:
            if role.name == "bot":
                member_count -= len(role.members)
        print((member_count // 2) + 1)
        if reaction.count >= ((member_count // 2) + 1):
            print(reaction.emoji.name)

    @commands.command()
    async def info(self, ctx: commands.Context):
        """   channelb = ctx.guild.get_channel(449750128073375775)
            message = await channelb.fetch_message(671177470359240706)
            print(message)
            for x in message.embeds:
                print(x.title)
                print(x.description)
                print(x.url)
        """
        
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("hello")

    @commands.command()
    async def r(self, ctx):
        self.bot.reload()


def setup(bot):
    bot.add_cog(Voting(bot))
