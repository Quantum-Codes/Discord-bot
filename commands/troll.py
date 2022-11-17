import discord

class troll(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot
  
  @discord.slash_command(name="token", description ="Reveal the bot's token")
  async def password(self, ctx):
    await ctx.respond("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983\nWhat did you expect?")

  @discord.slash_command(name="embedtest", description="haha", guild_ids =guild_ids)#delete later
  async def embedthing(self, ctx):
    embed=discord.Embed(title="Title ", url="https://ytvid.com", description="Desc", color=0xff0000)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Chess_x0t45.svg/1200px-Chess_x0t45.svg.png")
    embed.set_footer(text="Haha")
    await ctx.respond(embed=embed)




def setup(bot):
  bot.add_cog(troll(bot))