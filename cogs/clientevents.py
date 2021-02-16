import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
       print('I have been summoned')
 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, name='member')
        await member.add_role(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.channels:
            if str(channel) == "795986817097793557":
                await channel.send(f"{member.name} has left the server.")

def setup(client):
    client.add_cog(events(client)) 