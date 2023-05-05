# New code for unknown bot!
The old code is [here](https://github.com/Quantum-Codes/Discord-bot-old) 

This bot can:<br>
<ol>
<li>Play music</li>
<li>Tell jokes</li>
<li>Tell facts</li>
<li>Flip a coin</li>
<li>Generate random numbers</li>
<li>Reveal its token(??) - try this out lol</li>
</ol>

# Running locally
1. Download the code locally and install dependencies using poetry `poetry install`
2. Create a discord bot account using these [steps](https://discordpy.readthedocs.io/en/stable/discord.html).
3. Additionally in the `https://discord.com/developers/applications/<application id>/bot` bot page, tick all 3 intents then regenerate token.
4. Create a `.env` file
5. Add to `.env`:
```
token=<insert your token>
```
7. Uncomment lines 4 and 5.
8. Run `main.py`. It will take about 1 hour to register global commands to discord. If you need this to be instantaneous, then scroll down to "converting to local command"

# Running on replit
1. Create a python repl and in the shell git clone this repo.
2. Go to `replit.nix` and add `pkgs.ffmpeg` in
3. Go to `.replit` and set `guessImports = false`, `run = "python main.py"`
4. Run the repl
5. Also to keep it online, you should probably use replit deployments or point a pinger to the webpage created by the program.

# Converting to local commands 

You can replace content of `guild_ids` in `main.py` and add `guild_ids = guild_ids` in each decorator in `/commands` to convert them to local commands to run them immediately.

Eg: `@discord.slash_command(name="hello")` --> `@discord.slash_command(name="hello", guild_ids=guild_ids)`
