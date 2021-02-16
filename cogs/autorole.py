import discord
from discord.ext import commands
import utils


class autorole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.gulid.roles, name='member')
        await member.add_role(role)


def setup(client):
    client.add_cog(autorole(client))
