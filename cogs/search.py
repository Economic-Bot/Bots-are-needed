import discord
from discord.ext import commands
from youtubesearchpython import VideosSearch
import json
from disputils import BotEmbedPaginator


class Search(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def search(self, ctx, *stuff):
        stuff = " ".join(stuff)
        result_ = VideosSearch(stuff, limit=10)

        res = result_.result()
        results = [
            f'[{i+1}) {res["result"][i]["title"]}'
            f'{res["result"][i]["title"]}]'
            f'({res["result"][i]["link"]})'

            for i in range(
                len(res["result"])
            )
        ]

        embeds = [
            discord.Embed(
                title="Results:",
                description="\n".join(results[:5]),
                color=discord.Color.random()),

            discord.Embed(
                title="Results:",
                description="\n".join(results[5:]),
                color=discord.Color.random())
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()


def setup(client):
    client.add_cog(Search(client))
