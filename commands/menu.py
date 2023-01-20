import discord, re, json
from commands.voice import regex, join, get_video
from components.buttons import PlayButton

regex = f"""{regex.replace("^","").replace("$","")}"""
#print(regex)
link = re.compile(regex)

link = re.compile(regex.replace("$","").replace("^",""))

# here's a fail attempt at playlists

async def play(ctx, url, next):
  if ctx.author.voice:
    await join(ctx)
  else:
    await ctx.followup.send("First join a voice channel.")
    return

  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  
  video = get_video(url)
  discord.opus.load_opus("./libopus.so.0.8.0")
  ctx.voice_client.stop()
  ctx.voice_client.play(discord.FFmpegPCMAudio(video["stream_url"], **FFMPEG_OPTIONS), after= next)
  embed=discord.Embed(title=f"Playing: {video['title']}", url=video['webpage_url'], description=video['description'][:500], color=0xff0000)
  embed.set_thumbnail(url=video["thumbnail"]) 
  embed.set_footer(text=f"Views: {video['view_count']}")
  await ctx.followup.send(embed=embed, view = PlayButton())

async def playall(ctx, videos):
  x = videos.pop(0)
  await play(ctx, x, next= lambda e: playall(ctx, videos))

class menu(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot
  
  @discord.message_command(name="QueuePlay", guild_ids=guild_ids)
  async def linker(self, ctx, message):
    await ctx.defer()
    matches=[]
    for I in message.content.strip().split():
      x = link.match(I)
      if x:
        matches.append(x.group(0))
    await ctx.followup.send("**Playlist:\n**"+"\n".join(matches))
    playall(ctx, matches)

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

    

def setup(bot):
  bot.add_cog(menu(bot))