import discord
from discord.ext import commands
from disputils import BotEmbedPaginator

ec = """
**
?bag         
?bal         
?beg         
?bet         
?buy         
?dep            
?rob         
?sell        
?send        
?shop        
?withdraw   
**
"""

misc = """
**
?eval 
?ping     
?server_info
?uptime   
?whois
?poke
?invite or ?in
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
            discord.Embed(title="Misc Commands:",
                          description=misc,
                          color=discord.Color.gold()),
            discord.Embed(title="Music Commands:",
                          description=music__,
                          color=discord.Color.gold()),
            discord.Embed(title="Economy commands:",
                          description=ec,
                          color=discord.Color.gold()),
            discord.Embed(title="Moderation commands:",
                          description=mod,
                          color=discord.Color.gold())
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()


def setup(cl):
    cl.add_cog(help__(cl))
