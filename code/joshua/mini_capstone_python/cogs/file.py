import discord
from discord.ext import commands

class Random(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events w/ Cogs
    # @commands.Cog.listener()  # decorator to run a cog for event
    # async def on_ready(self):
    #     print('Bot is ready.')

    '''/////COMMANDS FOR ALL MEMBERS/////'''
    # Commands w/ Cogs
    @commands.command()       # decorator to run a cog for command
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()     
    async def broom(self, ctx):       # .broom using cog
        await ctx.send('You\'re a wizard, Harry!')

def setup(client):
    client.add_cog(Random(client))