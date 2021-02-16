import discord
from discord.ext import commands
import random
import aiohttp


class aitest(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ai"])
    async def ai_chat(self, ctx, *stuff):
        """Allowing user to chat with the bot"""

        async with ctx.typing():
            ai_url = f"http://bruhapi.xyz/cb/{'/'.join(stuff)}"

            async with aiohttp.ClientSession() as cs:
                async with cs.get(ai_url) as r:
                    response = await r.json()
                    # getting the `useful` response
                    result = response.get(
                        "res", "idk what you are saying :thinking:")

                    await ctx.send(f"{result}")


def setup(client):
    client.add_cog(aitest(client))
 