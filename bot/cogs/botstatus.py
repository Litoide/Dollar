#botstatus.py

import discord
import asyncio
import asyncpg
from discord.ext import commands, tasks
from itertools import cycle

status = cycle([
    'The longer the peso stays on earth, the more devalued it will become',
    'BUT MCREEEEEEE',
    'Eating your sueldo',
    'Argentina must devalue her currency to pay her debts! *cries in gringo*',
    'Los que tienen plata consumen de la buena',
    'Hasta que no sean Venezuela no paro',
    'In God We Trust',
    'Nisman se mató o lo mataron?',
    'Execute Order 66',
    "The most terrifying words in the English language are: I'm from the government and I'm here to help."
])


class Botstatus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.change_status.start()

    #COMMANDS
    @commands.Cog.listener()
    async def on_ready(self):
        print('botstatus load')

    #TASKS
    #@tasks.loop(seconds)

    @tasks.loop(seconds=60.0)
    async def change_status(self):
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(next(status)))

def setup(bot):
    bot.add_cog(Botstatus(bot))
