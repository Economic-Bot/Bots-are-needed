import discord
from discord.ext import commands


class Rick_Roll(commands.Cog):
 
 
 

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["doggy", "dogg"])
    async def dog(self, ctx, mentioned=None):
        if mentioned:
            await ctx.send(f"<@{ctx.author.id}> sent you: ||<a:rickroll:792418332326363136>|| {mentioned}")

        else:
            await ctx.send("<a:rickroll:792418332326363136>")


def setup(client):
    client.add_cog(Rick_Roll(client))
