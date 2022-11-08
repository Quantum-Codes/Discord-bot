import discord, random, requests

def _joke(typeofjoke):
  x = requests.get(f"https://official-joke-api.appspot.com/jokes/{typeofjoke}/random")
  if x.status_code != 200:
    return "An error has occurred. please try again later."
  x = x.json()
  if len(x) == 0:
    return "An error has occurred. please try again later."
  x = x[0]
  return [x["setup"],x["punchline"]]

def _fact():
  x = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
  if x.status_code != 200:
    return f"An error has occurred. please try again later. {x.status_code}"
  else:
    return x.json()["text"]

class general(discord.Cog):
  guild_ids = [871696913987162112]
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(name = "hello", description = "Say hello to the bot")
  async def hello(self, ctx):
    await ctx.respond("Hey!")

  @discord.slash_command(name="fact", description = "Tells a useless fact", guild_ids=guild_ids)
  async def fact(self, ctx):
    await ctx.respond(_fact())

  @discord.slash_command(name="coinflip", description = "Flips a virtual coin", guild_ids=guild_ids)
  async def flipcoin(self, ctx):
    heads_tails = ('Heads', 'Tails')
    choice = random.choice(heads_tails)
    await ctx.respond(f"You got a {choice}!")
    

  @discord.slash_command(name="rand", description="Pick a random number")
  async def rand(self, ctx, num1: int = 0, num2: int = 10):
    if num2 < num1:
      num1, num2 = num2, num1
    random_number = random.randint(num1, num2)
    await ctx.respond(str(random_number))

  @discord.slash_command(name="joke", description="Tells a joke", guild_ids=guild_ids)
  @discord.option("type", description="Type of joke", choices=["general", "programming", "knock-knock"])
  async def joke(self, ctx, type:str="general"):
    res = _joke(type)
    if "error" in res:
      await ctx.respond(f"{ctx.author.mention} {res}.\n type `!help joke` for info on command.")
    else:
      await ctx.respond(f"{ctx.author.mention}\n{res[0]}\n{res[1]}")


def setup(bot):
  bot.add_cog(general(bot))