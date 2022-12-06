import discord, re
from commands.voice import regex

link = re.compile(regex.replace("$","").replace("^",""))

class menu(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot
  
  @discord.message_command(name="linkfinder", guild_ids=guild_ids)
  async def linker(self, ctx, message):
    await ctx.respond(link.search(message.content))
    



def setup(bot):
  bot.add_cog(menu(bot))