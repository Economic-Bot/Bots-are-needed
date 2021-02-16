import discord
from discord.ext import commands


class Server_info(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    # to get the server info
    @commands.command(aliases=['info', 'serverinfo'])
    async def server_info(self, ctx):
        '''gives some information of the server'''

        name = str(ctx.guild.name)
        # description of the server
        description = "This server was meant for group studying and having fun" or str(
            ctx.guild.description)

        owner = str(ctx.guild.owner)  # owner name
        region = str(ctx.guild.region)  # server location

        member_count = str(ctx.guild.member_count)  # total members
        icon = str(ctx.guild.icon_url)  # server icon

        id_ = str(ctx.guild.id)
        embed = discord.Embed(
            title=f"{name} Server information",
            description=description,
            color=discord.Color.random()
        )

        embed.set_thumbnail(url=icon)  # the icon of the server
        embed.add_field(name="Owner", value=owner, inline=True)

        embed.add_field(name="Server id", value=id_, inline=True)
        embed.add_field(name="Region", value=region, inline=True)

        embed.add_field(name="Member count", value=member_count, inline=True)

        # sending the embed
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Server_info(client))
