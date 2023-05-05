import discord, re, asyncio
from commands.voice import regex
from commands.voice import play as voice

regex = f"""{regex.replace("^","").replace("$","")}"""
link = re.compile(regex)
link = re.compile(regex.replace("$","").replace("^",""))
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop) 

async def play_next(ctx, matches):
  matches.pop(0)
  if len(matches) == 0:
    return
  loop = asyncio.get_running_loop()
  await voice(ctx, matches[0], primary=False, next = lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx, matches), loop))


class menu(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot

  @discord.message_command(name="Play")
  async def linkerscan(self, ctx, message):
    matches=[]
    for I in message.content.strip().split():
      x = link.match(I)
      if x:
        matches.append(x.group(0))

    if len(matches) == 0:
      matches = ["invalid"]
    await voice(ctx, matches[0], next=None)

  @discord.message_command(name="Queued")
  async def queueplay(self, ctx, message):
    matches=[]
    for I in message.content.strip().split():
      x = link.match(I)
      if x:
        matches.append(x.group(0))
    
    if len(matches) == 0:
      matches = ["invalid"]
    loop = asyncio.get_running_loop()
    await voice(ctx, matches[0], next=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx, matches), loop), queue=matches)

def setup(bot):
  bot.add_cog(menu(bot))