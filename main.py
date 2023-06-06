#For replit only:
#make pycord work by making guessImports = false in .replit
#also add pkgs.ffmpeg in replit.nix for voice

import discord, os
from keep_alive import keep_alive
from components.buttons import SleepButton

if "REPL_SLUG" not in os.environ: #detect replit
  import dotenv
  dotenv.load_dotenv()
  


bot = discord.Bot()
guild_ids = [871696913987162112] #replace here

@bot.event
async def on_ready():
  print(f"{bot.user} is ready and online!")

@bot.event
async def on_message(message):
  if bot.user.mentioned_in(message):
    await message.reply("Why u pinged me? I was sleeping :( \n Make me sleep again", view=SleepButton())

@bot.event
async def on_voice_state_update(member, before, after):
  if after.channel: #joined
    if not bot.voice_clients and not after.channel.name.startswith("team"): #for a server
      await after.channel.connect()
  else: #left
    if len(before.channel.members) < 2: #after is None. so use before.
      for channel in bot.voice_clients:
        if channel.channel == before.channel:
          await channel.disconnect()


bot.load_extension("commands.general")
bot.load_extension("commands.troll")
bot.load_extension("commands.voice")
bot.load_extension("commands.menu")
keep_alive()
try:
  bot.run(os.environ["token"])
except discord.errors.HTTPException:
  os.system("kill 1")