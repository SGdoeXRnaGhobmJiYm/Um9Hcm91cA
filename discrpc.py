from discord.ext import commands
import discord, os
os.system('clear')
token = os.environ["TOKEN"]
bot = commands.Bot(command_prefix="-", case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Game(name="McGroups! ~ Group Finder", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")
    
bot.run(token)
