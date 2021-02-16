import discord
import random
from discord.ext import commands


class Who_is(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(aliases=["who"])  # whois command
    async def whois(self, ctx, user: discord.Member = None):
        """Shows when the user had created there account, and when the user joined the server"""

        User = user or ctx.author

        if User.bot:
            is_human = 'No'

        else:
            is_human = 'Yes'

        embed = discord.Embed(title=f'Discord Whois Complete',
                              description=f'The user looked up was: {User}', colour=discord.Color.gold(), inline=False)

        # embed.set_image(url=f'{avatar}')
        embed.add_field(name='Is this User a _human_ ?',
                        value=f'**{is_human}**', inline=False
                        )

        embed.add_field(name='Account Creation Date',
                        value=f'{User.created_at.strftime("%a, %d %B %Y , %I :%M %p UTC")}',
                        inline=False
                        )

        embed.add_field(
            name="Joined Server:",
            value=User.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC")
        )

        embed.set_thumbnail(url=User.avatar_url)

        embed.set_footer(
            icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}"
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Who_is(client))
