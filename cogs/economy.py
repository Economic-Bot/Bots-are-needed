import random
import json
import discord

from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.utils import get

import discord
from discord.ext import commands, tasks
import datetime

from asyncio import sleep

Bank = "./Jsons/mainbank.json"
Pets = "./Jsons/pets.json"

mainshop = [
    {"name": "Watch", "price": 30, "description": "Time"},
    {"name": "TV", "price": 340, "description": "Watch movies etc"},
    {"name": "Computer", "price": 90, "description": "To get memes"},
    {"name": "Laptop", "price": 60,
        "description": "To bet coins on memes which you think would be popular"}
]


class Ec(commands.Cog):

    def __init__(self, client):
        self.client = client

    # !-------Setting Up Economy-------!#
    async def open_account(self, user):

        users = await self.get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 100
            users[str(user.id)]["bank"] = 50

        with open(Bank, "w") as f:
            json.dump(users, f, indent=4)
        return True

    async def get_bank_data(self):
        with open(Bank, "r") as f:
            users = json.load(f)

        return users

    async def update_bank(self, user, change=0, mode="wallet"):
        users = await self.get_bank_data()

        users[str(user.id)][mode] += change

        with open(Bank, "w") as f:
            json.dump(users, f, indent=4)

        bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
        return bal

    @commands.command()
    async def beg(self, ctx):

        user = ctx.author

        await self.open_account(ctx.author)

        users = await self.get_bank_data()

        try:
            with open(Pets, "r") as f:
                petdata = json.load(f)

            pet_multi = petdata[str(ctx.author.id)]["Multi"]
            print("petversion")

            adderearnings = random.randrange(1, 400)
            realearnings = adderearnings * pet_multi
            earnings = adderearnings + realearnings

            # *-------------------------LIST OF RESPONSES----------------------------------------

            begResponses = [

                f"An ugly lady gave you **{int(earnings)}**$",
                f"**Tiktok Hoe: ** gave you **{earnings}**$",
                f"**Hungry Hipo: ** ......here is **{int(earnings)}**$ now get away",
                f"**SirBrozHeart: ** ...WHY U MAD, here is... **{earnings}**$ im retarded! jk but....im mad",
                f"**PizzaBoi: ** *dude im poor too, ima give you whatever i get from this guy.......*2 minutes later*...hey guy here is **{earnings}**$ enjoy",
                f"**a group of idiots :** ................just....ass...like imagine being poor, just here dude....ugh lets get of here... the idiot dontated **{earnings}**$ btw",
                f"**John Thicc: ** ..EXTRA THICCC, i mean you do be looking kinda THICC, so here {earnings}$",
                f"**Super Mario Thicc: ** **what's up homie.....SUPER MARIO HERE TAKE THE MONEY BYEEEEE {earnings}$",
                f"**bob: ** ....hey wanna hang out in my trash area....there is {earnings}$ there",
                f"**Eshadow: ** there is like 10 responses what a dead bot wowoowowow take this mother fucker... {earnings}$",
                f"**AINME DWEEB** hey wanna watch some anime? no? well fuck u and here is {earnings}$ and you're a bitch",
                f"A rich man has just been shot and {int(earnings)}$ has went on the floor!",

                f"Cool Boy Jacob: Sup dude, you begging like a loser, anyway here have{int(earnings)}$ so you dont bother me again.",

                f"Jeff Bezos: Your amazon order has been delivered, I'll give you {int(earnings)}$ to be generous",
                f"I'm giving you **{int(earnings)}**, now stay here for me to post it on insta $",
                f"Look, I am humble kiddo get these **{int(earnings)}** $",
                f"What about these **{int(earnings)}** , are these enough $"

            ]

            nomoneyresponse = [
                f"I think I'm gonna join you in the begging business; I am broke myself $",
                f"Ah yes, the negotiator $", f"Get a job bimbo $",
                f"I guess I won't give lol $",
                f"Oh you again, still **NO** $",
                f"All I can give is a hug *hugs lovely* $",
                f"Let's goooo another one to annoy my life, get away $",
                f"What can I say except get the fuck away $"]

            # *----------------------------------------------------------------------------------
            nomoneyrespon = random.choice(nomoneyresponse)
            begR = random.random.choice(begResponses)

            sleep(0.5)

            if earnings > 100:

                em = discord.Embed(
                    title="Beg", description=f"{begR}", color=discord.Color.random())
                em.set_footer(
                    text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=em)

                await self.update_bank(ctx.author, adderearnings)
            else:
                em = discord.Embed(
                    title="Beg", description=f"{nomoneyrespon}", color=discord.Color.random())
                em.set_footer(
                    text=f"Rquested by {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=em)

        except Exception:

            adderearnings = random.randrange(1, 200)
            earnings = adderearnings
            # *-------------------------LIST OF RESPONSES----------------------------------------

            begResponses = [

                f"An ugly lady gave you **{int(earnings)}**$",
                f"**Tiktok Hoe: ** gave you **{earnings}**$",
                f"**Hungry Hipo: ** ......here is **{int(earnings)}**$ now get away",
                f"**SirBrozHeart: ** ...WHY U MAD, here is... **{earnings}**$ im retarded! jk but....im mad",
                f"**PizzaBoi: ** *dude im poor too, ima give you whatever i get from this guy.......*2 minutes later*...hey guy here is **{earnings}**$ enjoy",
                f"**a group of idiots :** ................just....ass...like imagine being poor, just here dude....ugh lets get of here... the idiot dontated **{earnings}**$ btw",
                f"**John Thicc: ** ..EXTRA THICCC, i mean you do be looking kinda THICC, so here {earnings}$",
                f"**Super Mario Thicc: ** **what's up homie.....SUPER MARIO HERE TAKE THE MONEY BYEEEEE {earnings}$",
                f"**bob: ** ....hey wanna hang out in my trash area....there is {earnings}$ there",
                f"**Eshadow: ** they aer like 10 responses what a dead bot wowoowowow take this mother fucker... {earnings}$",
                f"**AINME DWEEB** hey wanna watch some anime? no? Well fuck you and here is {earnings}$ and you're a bitch",
                f"A rich man has just been shot and {int(earnings)}$ has went on the floor!",

                f"Cool Boy Jacob: Sup dude, you begging like a loser, anyway here have{int(earnings)}$ so you dont bother me again.",

                f"Jeff Bezos: Your amazon order has been delivered, I'll give you {int(earnings)}$ to be generous",
                f"I'm giving you **{int(earnings)}**, now stay here for me to post it on insta $",
                f"Look, I am humble kiddo get these **{int(earnings)}** $",
                f"What about these **{int(earnings)}** , are these enough $"

            ]

            nomoneyresponse = [

                f"I think I'm gonna join you in the begging buisness; I am broke myself $",
                f"Ah yes, the negotiator $",
                f"Get a job bimbo $"
                f"I guess I won't give lol $",
                f"Oh you again, still **NO** $",
                f"All I can give is a hug *hugs lovely* $",
                f"Let's goooo another one to annoy my life, get away $",
                f"What Can I say except get the fuck away $",

            ]

            # *----------------------------------------------------------------------------------
            nomoneyrespon = random.choice(nomoneyresponse)
            begR = random.random.choice(begResponses)

            if earnings > 100:
                em = discord.Embed(
                    title="Beg", description=f"{begR}", color=discord.Color.random())
                em.set_footer(
                    text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=em)
                await self.update_bank(ctx.author, adderearnings)
                await ctx.send("You can get more money by getting a pet!")

            else:
                em = discord.Embed(
                    title="Beg", description=f"{nomoneyrespon}", color=discord.Color.random())
                em.set_footer(
                    text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=em)

    @commands.command()
    async def rob(self, ctx, member: discord.Member):
        await self.open_account(ctx.author)
        await self.open_account(member)
        user = ctx.author

        bal = await self.update_bank(member)

        if ctx.author == member:
            await ctx.send("are you fucking trying to rob yourself...what...WHAT")

        else:
            bal[0] = int(bal[0])
            if bal[0] < 100:
                await ctx.send("he is poor it wont be worth it")
                return

            else:
                earnings = random.randint(0, bal[0])

                if earnings < 150:
                    print(earnings)
                    earnings = random.randint(60, bal[0])
                    await self.update_bank(ctx.author, -1 * earnings)
                    await self.update_bank(member, earnings)
                    embed = discord.Embed(title="Rob",
                                          description=f"You got caught and paid {earnings}$ to {member.mention}")
                    embed.set_footer(
                        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

                elif earnings > 7000:
                    earnings = random.randint(0, 7000)
                    print(earnings)
                    embed = discord.Embed(title="Rob", description=f"You Robbed {member.mention} and got {earnings}$",
                                          color=discord.Color.random())
                    embed.set_footer(
                        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    await self.update_bank(ctx.author, earnings)
                    await self.update_bank(member, -1 * earnings)

                else:
                    embed = discord.Embed(title="Rob", description=f"You Robbed {member.mention} and got {earnings}$",
                                          color=discord.Color.random())
                    embed.set_footer(
                        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    await self.update_bank(ctx.author, earnings)
                    await self.update_bank(member, -1 * earnings)
                    print(earnings)


    @commands.command()
    async def bet(self, ctx, amount):

        await self.open_account(ctx.author)

        user = ctx.author

        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        bal[1] = int(bal[1])

        if bal[0] < 99:
            await ctx.send("Sorry man, you gotta at least have 100$")
            return

        if amount < 99:
            await ctx.send("You have to bet 100$ or higher")

        if amount > 99 and bal[0] > 99:
            if amount > bal[0]:
                await ctx.send(
                    f"Bro you don't even have that much money my dud, you have only {bal[0]}$ and you're trying to bet {amount}$ tf?")
            else:

                Chance = random.randint(1, 2)

                if Chance == 1:
                    await ctx.send(f"Sorry you lost {amount}$")
                    await self.update_bank(ctx.author, -1 * amount)

                if Chance == 2:
                    await ctx.send(f"You won {amount}$")
                    await self.update_bank(ctx.author, amount)

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def send(self, ctx, member: discord.Member, amount=None):
        await self.open_account(ctx.author)
        await self.open_account(member)

        bal = await self.update_bank(ctx.author)
        if amount == "all":
            amount = bal[0]

        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("You're Poor")
            return

        if amount < 0:
            await ctx.send("You're Poor")
            return

        await self.update_bank(ctx.author, -1 * amount, "bank")
        await self.update_bank(member, amount, "bank")

        bal = await self.update_bank(ctx.author)

        await ctx.send(f"You Deposited {amount}$ to {member.mention}")

    @commands.command(aliases=["pos"])
    @commands.cooldown(1, 80, commands.BucketType.user)
    async def post(self, ctx):
        user = ctx.author

        users = await self.get_bank_data()

        bal = await self.update_bank(ctx.author)

        try:
            with open(Pets, "r") as f:
                petdata = json.load(f)

            pet_multi = petdata[str(ctx.author.id)]["Multi"]
            print("petversion")

            with open("./Jsons/mainbank.json", "w") as f:
                json.dump(users, f, indent=4)

            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]

                if n == "Pc":
                    print("petverios")
                    await ctx.send("TIME TO POST MEME")
                    sleep(2)
                    MEMEearningsR = random.randint(0, 1200)
                    mem = MEMEearningsR * pet_multi
                    MEMEearnings = MEMEearningsR + mem

                    if MEMEearnings > 500:
                        await ctx.send(f"Ay my boi..u is got alot of moneyyyy, **{MEMEearnings}$** to be exact my dud")
                        await self.update_bank(ctx.author, MEMEearnings)

                    elif MEMEearnings < 400:
                        MEMEearningsR = random.randint(400, 1200)
                        await ctx.send(
                            f"SO YOUR MEME SUCKED SO MUCH ASS THAT THE MEME POLICE GAVE YOU A FINE OF -**{MEMEearnings}$** BECAUSE UR MEME WAS ASS")
                        await self.update_bank(ctx.author, -1 * MEMEearnings)

        except Exception:

            with open("./Jsons/mainbank.json", "w") as f:
                json.dump(users, f, indent=4)

            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]

                if n == "Pc":
                    await ctx.send("TIME TO POST MEME")
                    sleep(2)
                    MEMEearnings = random.randint(0, 1200)

                    if MEMEearnings > 500:
                        await ctx.send(f"Ay my boi..u is got alot of moneyyyy, **{MEMEearnings}$** to be exact my dud")
                        await self.update_bank(ctx.author, MEMEearnings)

                    elif MEMEearnings < 400:
                        MEMEearningsR = random.randint(400, 1200)
                        await ctx.send(
                            f"SO YOUR MEME SUCKED SO MUCH ASS THAT THE MEME POLICE GAVE YOU A FINE OF -**{MEMEearnings}$** BECAUSE UR MEME WAS ASS")
                        await self.update_bank(ctx.author, -1 * MEMEearnings)

    @commands.command()
    async def bal(self, ctx):
        await self.open_account(ctx.author)

        users = await self.get_bank_data()

        wallet_amt = users[str(ctx.author.id)]["wallet"]
        bank_amt = users[str(ctx.author.id)]["bank"]

        embed = discord.Embed(
            title=f"{ctx.author}'s balance",
            color=discord.Color.red()
        )

        embed.add_field(name="Wallet balance:", value=wallet_amt)
        embed.add_field(name="Bank balance:", value=bank_amt)

        # sending the embed
        await ctx.channel.send(embed=embed)

    # to deposit money
    @commands.command(aliases=['depo', 'deposit'])
    async def dep(self, ctx, amount=None):
        # check whether account exists
        await self.open_account(ctx.author)

        if amount == None:  # no amount is given
            await ctx.channel.send(f'Please enter a amount !! <@{ctx.author.id}>')
            return

        if int(amount) < 0:  # negative amount is given
            await ctx.channel.send(f'Please enter a _positive amount_ !! <@{ctx.author.id}>')
            return

        # getting bank details
        bal = await self.update_bank(ctx.author)

        # 0 --> wallet
        # 1 --> bank

        amount_ = int(amount)
        if amount_ > bal[0]:
            await ctx.channel.send(f"You don't have enough funds !!! <@{ctx.author.id}>")
            return

        # decreasing wallet balance
        await self.update_bank(ctx.author, -1*amount_)

        # increasing bank balance, duality principle
        await self.update_bank(ctx.author, amount_, "bank")

        # telling that he/she has with drawn <amount_>
        await ctx.channel.send(f"You deposited {amount_} coins !! <@{ctx.author.id}>")

    # to withdraw money
    @commands.command(aliases=['withdrew', 'wit'])
    async def withdraw(self, ctx, amount=None):
        # check whether account exists
        await self.open_account(ctx.author)

        if amount == None:  # no amount is given
            await ctx.channel.send(f'Please enter a amount !! <@{ctx.author.id}>')
            return

        if int(amount) < 0:  # negative amount is given
            await ctx.channel.send(f'Please enter a _positive amount_ !! <@{ctx.author.id}>')
            return

        # getting bank details
        bal = await self.update_bank(ctx.author)

        # 0 --> wallet
        # 1 --> bank

        amount_ = int(amount)
        if amount_ > bal[1]:
            await ctx.channel.send(f"You don't have enough funds !!! <@{ctx.author.id}>")
            return

        # increasing wallet balance
        await self.update_bank(ctx.author, amount_)

        # decreasing bank balance, duality principle
        await self.update_bank(ctx.author, -1*amount_, "bank")

        # telling that he/she has with drawn <amount_>
        await ctx.channel.send(f"You withdrew {amount_} coins !! <@{ctx.author.id}>")

    # to show the things user could buy
    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(
            title="Shop", description="Things which you could buy: ")

        for item in mainshop:
            name = item["name"]
            price = item["price"]
            desc = item["description"]
            embed.add_field(name=name, value=f"${price} \n{desc}", inline=True)

        await ctx.channel.send(embed=embed)

    # to allow user to buy stiff
    @commands.command()
    async def buy(self, ctx, item, amount=1):
        await self.open_account(ctx.author)

        result = await self.buy_this(ctx.author, item, amount)

        if not result[0]:
            # if the item isn't there then:
            if result[1] == 1:
                await ctx.channel.send("That Object isn't there!")
                return

            # if there isn't enough money then
            if result[1] == 2:
                await ctx.channel.send(f"You don't have enough money in your wallet to buy {amount} {item}")
                return

        # showing what the user has bought
        await ctx.channel.send(f"You just bought {amount} {item}")

    # all checks etc on the things user buyied occurs here
    async def buy_this(self, user, item_name, amount):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()

            # check whether item exits
            if name == item_name:
                name_ = name
                price = item["price"]
                break

        # item doesn't exit
        if name_ == None:
            return [False, 1]

        # finding the total cost
        cost = price*amount

        users = await self.get_bank_data()

        bal = await self.update_bank(user)

        # checking whether the user has sufficient fund
        if bal[0] < cost:
            return [False, 2]

        try:
            index = 0
            t = None

            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]

                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt + amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break

                index += 1

            if t == None:
                obj = {"item": item_name, "amount": amount}
                users[str(user.id)]["bag"].append(obj)

        except Exception:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"] = [obj]

        with open(Bank, "w") as f:
            json.dump(users, f)

        await self.update_bank(user, cost*-1, "wallet")

        return [True, "Worked"]

    # to allow user to sell stuff

    @commands.command()
    async def sell(self, ctx, item, amount=1):
        await self.open_account(ctx.author)

        res = await self.sell_this(ctx.author, item, amount)

        if not res[0]:
            if res[1] == 1:
                await ctx.channel.send("That Object isn't there!")
                return
            if res[1] == 2:
                await ctx.channel.send(f"You don't have {amount} {item} in your bag.")
                return
            if res[1] == 3:
                await ctx.channel.send(f"You don't have {item} in your bag.")
                return

        await ctx.channel.send(f"You just sold {amount} {item}.")

    # to do checks on what the user is trying to sell
    async def sell_this(self, user, item_name, amount, price=None):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                if price == None:
                    price = 0.9 * item["price"]
                break

        if name_ == None:
            return [False, 1]

        cost = price*amount

        users = await self.get_bank_data()

        bal = await self.update_bank(user)

        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]

                # checking whether the item exists
                if n == item_name:

                    # the cost of that item
                    old_amt = thing["amount"]
                    new_amt = old_amt - amount

                    # checking whether there is enough funds
                    if new_amt < 0:
                        return [False, 2]

                    # changing the [total] amount to the new amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt

                    t = 1
                    break

                # index is used for going through the bag
                index += 1

            if t == None:
                return [False, 3]

        except Exception:
            return [False, 3]

        # storing the data
        with open(Bank, "w") as f:
            json.dump(users, f)

        # updating user's bank
        await self.update_bank(user, cost)

        # items were successfully sold
        return [True, "Worked"]

    # to allow user to see what they  have bought
    @commands.command(aliases=["inv"])
    async def bag(self, ctx):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        try:
            # check whether the user has bought anything
            bag = users[str(user.id)]["bag"]
        except Exception:
            # user hasn't bought anything
            bag = []

        embed = discord.Embed(
            title="Bag", description="All the things your have bought:", color=discord.Color.random())
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            embed.add_field(name=name, value=amount)

        # showing the things user had bought
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Ec(client))
