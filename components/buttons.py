import discord

class SleepButton(discord.ui.View):
    @discord.ui.button(label= "Put to sleep", style=discord.ButtonStyle.primary, emoji=None)
    async def button_callback(self, button, interaction):
      button.disabled = True
      button.label = "sleeping..."
      button.style = discord.ButtonStyle.success
      await interaction.response.edit_message(view=self)
      await interaction.followup.send("Thank you! 😴")

class PlayButton(discord.ui.View):
    @discord.ui.button(label= None, style=discord.ButtonStyle.primary, emoji="⏸")
    async def button_callback(self, button, interaction):
      print([i for i in str(button.emoji)])
      if str(button.emoji) == "⏸":
        button.emoji = "▶️"
        interaction.guild.voice_client.pause()
      else:
        button.emoji = "⏸"
        interaction.guild.voice_client.resume()
      await interaction.response.edit_message(view=self)