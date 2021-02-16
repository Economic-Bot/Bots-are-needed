import discord
from discord.ext import commands
import json
client = commands.Bot(command_prefix='')


class lvls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_member_join(self, member):
        with open(r"C:\Users\Frank\Desktop\BOTZS\test.py", 'r') as f:
            users = json.load(f)

        await update_data(users, member)

        with open('LvlUP.json', 'w') as f:
            json.dump(users, f)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            with open('LvlUP.json', 'r') as f:
                users = json.load(f)

            await update_data(users, message.author)
            await add_experience(users, message.author, 5)
            await level_up(users, message.author, message)

            with open('LvlUP.json', 'w') as f:
                json.dump(users, f)

    async def update_data(self, users, user):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 1

    async def add_experience(self, users, user, exp):
        users[f'{user.id}']['experience'] += exp

    async def level_up(self, users, user, message):
        experience = users[f'{user.id}']['experience']
        lvl_start = users[f'{user.id}']['level']
        lvl_end = int(experience**(1 / 4))
        if lvl_start < lvl_end:
            embed = discord.Embed(
                title="**LEVEL UP!**",
                description=
                f'{user.mention} has leveled up to level {lvl_end}! :fire: '
                f'\n Soundwave Superior,{user.mention} Inferior ',
                color=discord.Color.dark_red())
            embed.set_thumbnail(url=user.avatar_url)
            users[f'{user.id}']['level'] = lvl_end
            await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(lvls(client))
