import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events w/ Cogs
    @commands.Cog.listener()  # decorator to run a cog for event
    async def on_ready(self):
        print('Bot is ready.')

    # Commands w/ Cogs
    @commands.command()       # decorator to run a cog for command
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Example(client))