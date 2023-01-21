import discord, youtube_dl, re
from components.buttons import PlayButton

#https://stackoverflow.com/questions/60745020/is-there-a-way-to-directly-stream-audio-from-a-youtube-video-using-youtube-dl-or EPIC ANSWER

regex = "^(https:\/\/((www\.youtube\.com)|(youtu\.be))\/((watch\?v=)|())[a-zA-Z0-9]{11}$)"
link = re.compile(regex) #created, tested on epic site https://regex101.com/r/zdMkMw/1

async def join(ctx):
  if ctx.voice_client:
    await ctx.voice_client.move_to(ctx.author.voice.channel)
  else:
    await ctx.author.voice.channel.connect()

def get_video(url):
  ydl_opts = {'format': 'bestaudio/best', 'restrictfilenames': True, 'noplaylist': True, 'nocheckcertificate': True, 'ignoreerrors': False, 'logtostderr': False, 'quiet': True, 'no_warnings': True, 'default_search': 'auto', 'source_address': '0.0.0.0','force-ipv4': True, 'cachedir': False}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     song_info = ydl.extract_info(url, download=False)

  keys = ["title", "thumbnail", "description", "upload_date", "view_count", "webpage_url"]
  video = {}
  for item in keys:
    video[item] = song_info[item]

  video["stream_url"] = song_info["formats"][0]["url"]
  return video

async def play(ctx, url:str, next=None, queue=None):
  await ctx.defer()
  if ctx.author.voice:
    await join(ctx)
  else:
    await ctx.followup.send("First join a voice channel.")
    return

  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
  if not link.match(url):
    await ctx.followup.send("Seems like an invalid YouTube video link.. If it isn't, then contact my developer. \n Links are usually of the format: \n`https://youtu.be/<id>`\n`https://www.youtube.com/watch?v=<id>`\n`https://www.youtube.com/watch?v=<id>`")
    return 

  video = get_video(url)
  discord.opus.load_opus("./libopus.so.0.8.0")
  ctx.voice_client.stop()
  ctx.voice_client.play(discord.FFmpegOpusAudio(video["stream_url"], **FFMPEG_OPTIONS), after=next)
  
  embed=discord.Embed(title=f"Playing: {video['title']}", url=video['webpage_url'], description=video['description'][:500], color=0xff0000)
  embed.set_thumbnail(url=video["thumbnail"]) 
  embed.set_footer(text=f"Views: {video['view_count']}")
  if queue is None:
    msg = ""
  else:
    msg = "**Playlist:**\n"+"\n".join(queue)
  await ctx.followup.send(msg, embed=embed, view = PlayButton())


class voice(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot
  
  @discord.slash_command(name="join", description ="Join voice channel")
  async def join(self, ctx):
    await ctx.defer()
    if ctx.author.voice:
      await join(ctx)
      await ctx.followup.send("Joined voice channel")
    else:
      await ctx.followup.send("Join a voice channel first! Then run this command.")

  @discord.slash_command(name="leave", description="Leave the voice channel")
  async def leave(self, ctx):
    if ctx.voice_client:
      await ctx.guild.voice_client.disconnect()
      await ctx.respond("Left voice channel")
    else:
      await ctx.respond("I'm not in a voice channel, use the /join command to make me join")

  @discord.slash_command(name="play", description = "play a YouTube song with url (later search will exist)", guild_ids=guild_ids)
  async def playsong(self, ctx, url:str):
    await play(ctx, url)
    
  @discord.slash_command(name="stop", description="Stops any playing sound")
  async def stop(self, ctx):
    if ctx.voice_client:
      ctx.voice_client.stop()
      await ctx.respond("Stopped any music")
    else:
      await ctx.respond("I don't think I'm in any voice channel.")

  @discord.slash_command(name="pause", description ="pauses any playing sound")
  async def pause(self, ctx):
    if ctx.voice_client:
      ctx.voice_client.pause()
      await ctx.respond("Paused any music")
    else:
      await ctx.respond("I don't think I'm in any voice channel.")

  @discord.slash_command(name="resume", description ="resumes any paused sound")
  async def resume(self, ctx):
    if ctx.voice_client:
      ctx.voice_client.resume()
      await ctx.respond("Resumed music")
    else:
      await ctx.respond("I don't think I'm in any voice channel.")


def setup(bot):
  bot.add_cog(voice(bot))