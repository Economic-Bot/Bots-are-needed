import discord
import random
from discord.ext import commands


class Guess_game(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    is_playing_guess = False  # to check whether a user is playing -> becomes true
    is_playing_guess_author = ''  # to store who is playing
    already_said_in_game = True  # to check whether `you are in a game` is said or not
    # -> becomes False

    @commands.Cog.listener()
    async def on_message(self, message):
        '''to check whether the user won or something'''

        author = message.author  # the author
        content = message.content  # the content
        number_bot = random.randint(1, 10)

        # the user is playing the the guessing game
        if self.is_playing_guess and self.already_said_in_game:
            already_said_in_game = False

        try:
            # the user guessed it
            if author.id == self.is_playing_guess_author and int(content) == number_bot:
                # return to default values
                self.already_said_in_game, self.is_playing_guess = True, False
                self.is_playing_guess_author = ''
                await message.add_reaction("🥳")
                return await message.channel.send(f"**You won !! <@{author.id}>** \<3")

            # the user didn't guess it yet
            if author.id == self.is_playing_guess_author and int(content) != number_bot:
                await message.channel.send(f"Nope, Try again <@{author.id}>")
        except ValueError:
            return await message.channel.send(f"Please enter a number between 0-8 <@{message.author.id}>, \nor do `?stop_guess` to stop playing the game")
            
    # to play the guessing game
    @commands.command(aliases=["guess"])
    async def play_guess(self, ctx):
        '''to allow user to join the game'''

        self.is_playing_guess = True
        self.is_playing_guess_author = ctx.author.id
        embed = discord.Embed(
            color=discord.Color.random()
        )

        embed.add_field(name=f'You are in the game now ! \nGuess a number between 0-10',
                        value=f"<@{ctx.author.id}>", inline=True)

        # sending the user  a message stating that they have joined the game
        await ctx.message.reply(embed=embed)

    # to stop playing the guessing game

    @commands.command()
    async def stop_guess(self, ctx):
        '''to allow the user to stop playing the guessing game'''

        # i've added this,so other users can't end the game, but only the player can
        if self.is_playing_guess:
            if ctx.author.id == self.is_playing_guess_author:
                # return to default values
                self.already_said_in_game, self.is_playing_guess = True, False
                self.is_playing_guess_author = ''
                await ctx.message.reply(f'You have left the game... <@{ctx.author.id}>')

            else:
                # the user isn't playing the game
                await ctx.message.reply(f'Your not playing the game !! <@{ctx.author.id}>')

        # if the user hadn't joined a game then
        else:
            await ctx.message.reply(f'First, Join a game !! <@{ctx.author.id}>')


def setup(client):
    client.add_cog(Guess_game(client))