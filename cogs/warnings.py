import discord
from discord.ext import commands
import json


class Warns(commands.Cog):
    def __init__(self, sht):
        self.client = sht

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def warn(self, ctx, user: discord.Member, *reason: str):
        if not reason:
            await ctx.send("Please provide a reason")
            return

        with open('reports.json', mode="a", encoding='utf-8') as f:
            try:
                report = json.load(f)
            except ValueError:
                report = {}
        
        report['users'] = []
        reason = ' '.join(reason)
        
        await user.send(f'you have been warned in {ctx.gulid.name} for {reason}')

        await ctx.send(
            (f'<@{user.id}> has been warned in {ctx.gulid.name} for {reason}'))

        for current_user in report['users']:
            if current_user['name'] == user.name:
                current_user['reasons'].append(reason)
                break
        else:
            report['users'].append({
                'name': user.name,
                'reasons': [
                    reason,
                ]
            })

        with open('reports.json', 'w') as f:
            json.dump(report, f)#hii

    async def warnings(self, ctx, user: discord.Member):
        with open('reports.json', mode="a", encoding='utf-8') as f:
            try:
                report = json.load(f)
            except ValueError:
                report = {}

        for current_user in report['users']:
            await ctx.send(current_user)


def setup(cl):
    cl.add_cog(Warns(cl))
