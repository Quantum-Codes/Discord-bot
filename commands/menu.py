import discord, re, json, asyncio
from commands.voice import regex, join, get_video
from commands.voice import play as voice
from components.buttons import PlayButton

regex = f"""{regex.replace("^","").replace("$","")}"""
#print(regex)
link = re.compile(regex)
link = re.compile(regex.replace("$","").replace("^",""))
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop) 

async def play_next(ctx, matches):
  matches.pop(0)
  if len(matches) == 0:
    return
  await ctx.send(f"Next song? {matches[0]}")
  loop = asyncio.get_running_loop()
  await voice(ctx, matches[0], next = lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx, matches), loop))


class menu(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot

  @discord.message_command(name ="ScanEmbed", guild_ids =[1017417232952852550])
  async def embedscan(self, ctx, message):
    content= message.embeds[0].to_dict()["description"]
    with open("embed.json", "w") as file:
      json.dump(content,file)
    patterns= (
      "They paid: `.[0-9,]{5,}`"
    )
    x = []
    for item in patterns:
      x.append(re.search(item, content).group(0))
      pass

    await ctx.respond("\n".join(x), ephemeral = True)

  @discord.message_command(name="Play", guild_ids=guild_ids)
  async def linkerscan(self, ctx, message):
    matches=[]
    for I in message.content.strip().split():
      x = link.match(I)
      if x:
        matches.append(x.group(0))
    await voice(ctx, matches[0], next=None)

  @discord.message_command(name="Queued", guild_ids=guild_ids)
  async def queueplay(self, ctx, message):
    matches=[]
    for I in message.content.strip().split():
      x = link.match(I)
      if x:
        matches.append(x.group(0))
    
    loop = asyncio.get_running_loop()
    await voice(ctx, matches[0], next=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx, matches), loop), queue=matches)

    

def setup(bot):
  bot.add_cog(menu(bot))