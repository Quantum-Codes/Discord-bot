import discord, re
from commands.voice import regex

regex = f"""{regex.replace("^","").replace("$","")}"""
#print(regex)
link = re.compile(regex)

class menu(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot
  
  @discord.message_command(name="linkfinder", guild_ids=guild_ids)
  async def linker(self, ctx, message):
    matches=[]
    for I in message.content.strip().split():
      matches.append(link.findall(I))
    await ctx.respond(str(" ".join(matches)))

def setup(bot):
  bot.add_cog(menu(bot))