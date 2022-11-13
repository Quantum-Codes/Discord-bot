import discord

class SleepButton(discord.ui.View):
    @discord.ui.button(label= "Put to sleep", style=discord.ButtonStyle.primary, emoji=None)
    async def button_callback(self, button, interaction):
      button.disabled = True
      button.label = "sleeping..."
      button.style = discord.ButtonStyle.success
      await interaction.response.edit_message(view=self)
      await interaction.followup.send("Thank you! 😴")
      