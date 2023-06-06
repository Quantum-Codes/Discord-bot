import discord

class selectmenu1(discord.ui.View):
    def __init__(self):
      super().__init__(timeout=10)
    async def on_timeout(self):
      self.disable_all_items()
      self.disable_on_timeout()

      await self.message.edit(view=self)
      


    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a Flavor!", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Strawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
    async def select_callback1(self, select, interaction): # the function called when the user is done selecting options
        self.disable_all_items()
        await interaction.response.edit_message(view=self)

        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")


    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a Flavor2!", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vanila",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Choolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Stawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
    async def select_callback2(self, select, interaction): # the function called when the user is done selecting options
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")
