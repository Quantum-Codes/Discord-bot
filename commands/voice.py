import discord

class voice(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot
  
  @discord.slash_command(name="join", description ="Join voice channel", guild_ids=guild_ids)
  async def join(self, ctx):
    connected = ctx.author.voice
    if connected:
      await connected.channel.connect()
      await ctx.respond("Joined voice channel")
    else:
      await ctx.respond("Join a voice channel first! Then run this command.")

  @discord.slash_command(name="leave", description="Leave the voice channel", guild_ids=guild_ids)
  async def leave(self, ctx):
    if ctx.voice_client:
      await ctx.guild.voice_client.disconnect()
      await ctx.respond("Left voice channel")
    else:
      await ctx.respond("I'm not in a voice channel, use the /join command to make me join")





def setup(bot):
  bot.add_cog(voice(bot))