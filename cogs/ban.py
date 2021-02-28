import discord
from discord.ext import commands

class banunban(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'{user.name } was baned for {reason}')
        await member.send(f'you have neen ban from  for {reason}')
        
    @commands.command()
    async def unban(self, *, ctx, member):
        banned_users = await ctx.gulid.bans()
        member_name, member_discriminator = member.split("a")
        
        for ban_entry in banned_users:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.gulid.unban(user)
                await ctx.send(f'{user.name} is unbaned')
            
def setup(client):
    client.add_cog(banunban(client))
        