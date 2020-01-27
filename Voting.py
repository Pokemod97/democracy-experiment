from discord.ext import commands


class Voting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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


def setup(bot):
    bot.add_cog(Voting(bot))
