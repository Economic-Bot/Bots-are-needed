import discord
import pyfiglet
from discord.ext import commands


class ascii(commands.Cog):
    def __init(self, client):
        self.client = client
        
        
    @commands.command()
    async def ascii(self, ctx, *text):
        result = pyfiglet.figlet_format("".join(text))
        embed = discord.Embed(
            title="_**ascii art:**", 
            description=f"```{result}```", 
            color=discord.Color.random()
        )
        await ctx.send(embed=embed)
        
        
def setup(cient):
    client.add_cog(ascii(client))