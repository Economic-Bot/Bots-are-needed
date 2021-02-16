import discord
from discord.ext import commands


class serverid(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def link(self, ctx, guild_id : int):
        guild = self.client.get_guild(guild_id)
        channel = guild.text_channels[0]
        link = await channel.create_invite(max_age = 0)
        await ctx.send(link)



def setup(client):
    client.add_cog(serverid(client))
