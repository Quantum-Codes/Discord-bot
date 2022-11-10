#make pycord work by making guessimports = false in .replit yay
import os
import discord
from keep_alive import keep_alive

bot = discord.Bot()
guild_ids = [871696913987162112]

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.load_extension("commands.general")
bot.load_extension("commands.troll")
keep_alive()
try:
  bot.run(os.environ["token"])
except discord.errors.HTTPException:
  os.system("kill 1")