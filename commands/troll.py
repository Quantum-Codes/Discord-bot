import discord
from main import guild_ids

class troll(discord.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @discord.slash_command(name="token", description ="Reveal the bot's token")
  async def password(self, ctx):
    await ctx.respond("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983\nWhat did you expect?")




def setup(bot):
  bot.add_cog(troll(bot))