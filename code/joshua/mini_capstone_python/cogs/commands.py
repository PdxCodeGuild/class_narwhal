import discord
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events w/ Cogs
    # @commands.Cog.listener()  # decorator to run a cog for event
    # async def on_ready(self):
    #     print('Bot is ready.')

    # Commands w/ Cogs
    @commands.command()       # decorator to run a cog for command
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('HOLA')

    # @commands.command()     # .broom using cog
    # async def broom(self, ctx):
    #     await ctx.send('You\'re a wizard, Harry!')

def setup(client):
    client.add_cog(Commands(client))