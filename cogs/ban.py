aimport discord
from discord.ext import commands


class All_Mod(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command() # uses command decorators, in this case inside a cog
    @commands.has_permissions(ban_members=True) # only people that have permissions to ban users can use this command
    async def ban(self, ctx, user: discord.Member, *, reason): # The person banning someone has to ping theuser to 
        await ctx.guild.ban(user, reason=reason) # Bans the user.
        await user.send(f"You have been banned in {ctx.guild} for {reason}") # Private messages user.
        await ctx.send(f"{user} has been successfully banned.") # messages channel to tell everyone it worked

    @commands.command(description="Kicks a member")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.send(f"You were kicked in the server {ctx.guild.name} for ****{reason}****")
        await member.kick(reason=reason)
        await ctx.send(f"{member} was kicked!")


def setup(cl):
    cl.add_cog(All_Mod(cl))
