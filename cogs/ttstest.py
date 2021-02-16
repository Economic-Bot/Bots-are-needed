import discord
from discord.ext import commands
import random
from gtts import gTTS


class TTS(commands.Cog):
    """To convert text to speech"""

    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def tts(self, ctx, *txt, **lang_):

        text = "".join(txt)
        tts = gTTS(text, lang=lang_.get("lang=", "en"))

        # saving the file
        tts.save("tts.mp3")

        # uploading file
        file = discord.File("tts.mp3")
        await ctx.send(file=file)


def setup(client):
    client.add_cog(TTS(client))
