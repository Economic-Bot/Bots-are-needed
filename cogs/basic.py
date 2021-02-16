from discord.ext import commands
import discord

# from utils import notify_user


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(brief="Creates an invite link to the channel")
    # @commands.guild_only()
    # async def invite(self, ctx):
    #     link = await ctx.channel.create_invite(max_age=1)
    #     await ctx.send(link)

    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            channel = member.dm_channel
            if channel is None:
                channel = await member.create_dm()
                await channel.send("%s poked you!!!!!!!!" % ctx.author.name)
        else:
           await ctx.send("please use @metion to poke someone")
           
         
def setup(bot):
    bot.add_cog(Basic(bot))
