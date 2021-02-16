import discord
from discord.ext import commands
import random


class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['in'])
    async def invite(self, ctx):
        """To allow people to invite this bot to other servers"""

        embed = discord.Embed(
            title='**Invite**',
            colour=discord.Color.blue()
        )

        embed.add_field(name='Bots Are Needed',
                        value='If you would like to invite me! \n[Click Here](https://discord.com/api/oauth2/authorize?client_id=782270717168582678&permissions=8&scope=bot)', inline=True)

        embed.set_thumbnail(
            url='https://cdn.discordapp.com/avatars/782270717168582678/6ecb133a2fbfa7f23b3a1118bcbc1d6b.webp?size=1024')

        embed.set_footer(text='Bot created by dragon_cai#2152')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Invite(client))
