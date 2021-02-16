import discord 
from discord.ext import commands


class ctx2(commands.Cog):

    def __init__ (self, client):
        self.client = client
        
        
    @commands.command()
    async def topgg(self, ctx):
         await ctx.send(f"please upvote and leave a review on https://top.gg/bot/782270717168582678")
         await client.add_rection("F")
         
      
def setup(client):
    client.add_cog(ctx2(client))