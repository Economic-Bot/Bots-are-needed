import discord
from discord.ext import commands


class bankickunban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.send(f'you have been kicked for **{reason}**')
        await member.kick(reason=reason)
        
        
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.send(f'you have been banned for **{reason}**')
        await member.ban(reason=reason)
        
        
def setup(client):
    client.add_cog(bankickunban(client))
 