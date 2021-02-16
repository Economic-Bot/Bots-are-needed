import discord
from discord.ext import commands

class sever(commands.Cog):
    def __init__(self, client):
        self.client = client   
    
    @commands.command()
    async def id(self, ctx):
        for guild in self.client.guilds:
            await ctx.send(guild.name)
            await ctx.send(guild.id)

def setup(bot):
    bot.add_cog(sever(bot))