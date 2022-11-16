import discord, youtube_dl

#https://stackoverflow.com/questions/60745020/is-there-a-way-to-directly-stream-audio-from-a-youtube-video-using-youtube-dl-or EPIC ANSWER

def get_video(url):
  ydl_opts = {'format': 'bestaudio', 'noplaylist': 'True'}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     song_info = ydl.extract_info(url, download=False)

  keys = ["title", "thumbnail", "description", "upload_date", "view_count", "webpage_url"]
  video = {}
  for item in keys:
    video[item] = song_info[item]

  video["stream_url"] = song_info["formats"][0]["url"]
  return video


class voice(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot
  
  @discord.slash_command(name="join", description ="Join voice channel", guild_ids=guild_ids)
  async def join(self, ctx):
    connected = ctx.author.voice
    if connected:
      if ctx.voice_client:
        await ctx.voice_client.move_to(connected.channel)
      else:
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

  @discord.slash_command(name="play", description = "play a YouTube song with url (later search will exist)", guild_ids=guild_ids)
  async def play(self, ctx, url:str):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    voice = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      discord.opus.load_opus("./libopus.so.0.8.0")
      voice.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS))




def setup(bot):
  bot.add_cog(voice(bot))