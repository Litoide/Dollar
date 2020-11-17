# dolar.py
import discord
import os
import asyncio
import asyncpg
from discord.ext import commands

from dotenv import load_dotenv


load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Growing stronger'))
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await asyncio.sleep(1)
    bot.load_extension(f'cogs.{extension}')


for filename in os.listdir('bot/cogs'): #'bot/cogs' # './cogs'
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
