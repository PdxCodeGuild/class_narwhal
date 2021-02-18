import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    def is_it_me(ctx):
        return ctx.author.id == 334183722763026433

    '''/////COMMANDS FOR DEV/ADMIN/////'''
    @commands.command()
    @commands.check(is_it_me)
    async def test(self, ctx):
        await ctx.send(f'Hi I am {ctx.author}!')

    @commands.command()
    @commands.check(is_it_me)
    async def test2(self, ctx):
        await ctx.send('This is a test.')

    @commands.command()
    @commands.check(is_it_me)
    async def test3(self, ctx):
        await ctx.send('TEST')

def setup(client):
    client.add_cog(Test(client))