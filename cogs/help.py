import discord
from discord.ext import commands
from disputils import BotEmbedPaginator

ec = """"
**
?bag         
?bal         
?beg         
?bet         
?buy         
?dep         
?gamble      
?post        
?rob         
?sell        
?send        
?shop        
?withdraw   
**
"""

fun = """
**
?eval 
?ping     
?server_info
?uptime   
?whois
?meme 
?poke
?invite or ?in
?ai 
?id 
?tts
**
"""

mod = """
**
?ban         
?kick 
?change_prefix
**
"""

music__ = """
**
?join       
?leave       
?loop        
?now         
?pause       
?play       
?queue       
?remove      
?resume      
?shuffle     
?skip       
?stop        
?summon      
?volume   
**
"""


class help__(commands.Cog):
    def __init__(self, cl):
        self.client = cl

    @commands.command()
    async def help(self, ctx):
        embeds = [
            discord.Embed(
                title="Here are all the commands",
                description="Click the arrows to navigate through the commands",
                color=discord.Color.gold()),
            discord.Embed(title="Fun commands:",
                          description=fun,
                          color=discord.Color.gold()),
            discord.Embed(title="Music commands:",
                          description=music__,
                          color=discord.Color.gold()),
            discord.Embed(title="Economic commands:",
                          description=ec,
                          color=discord.Color.gold()),
            discord.Embed(title="Moderator commands:",
                          description=mod,
                          color=discord.Color.gold())
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()


def setup(cl):
    cl.add_cog(help__(cl))
