import discord 
from discord.ext import commands


class ctx(commands.Cog):

    def __init__ (self, client):
        self.client = client
        
        
    @commands.command()
    async def f(self, ctx):
         await ctx.send(f"<@{ctx.author.id}> f")
         await client.add_rection("F")
         
      
def setup(client):
    client.add_cog(ctx(client))
