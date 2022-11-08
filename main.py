#make pycord work by making guessimports = false in .replit
import os
import discord
from keep_alive import keep_alive

bot = discord.Bot()
guild_ids = [871696913987162112]

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.load_extension("commands.general")
keep_alive()
bot.run(os.environ["token"])