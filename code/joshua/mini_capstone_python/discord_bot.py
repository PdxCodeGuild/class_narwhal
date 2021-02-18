'''
Josh Novac
Python Mini Capstone
Python
PDX Code Guild
'''

import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
## status cycling through two. every 10 seconds ##
status = cycle(['Admin', 'Bot'])  # task @ line 47

'''/////EVENTS/////
---------------------------------------------------------------------
'''
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')
    await ctx.send(f'Welcome {member}!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a TEST.')

'''
/////TASKS/////
---------------------------------------------------------------------
'''
# task that loops a change of status for bot every 10 seconds
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

'''/////COMMANDS/////
---------------------------------------------------------------------
'''

""" - BEFORE COGS -
@client.command()     # client decorator for command in discord
async def ping(ctx):   # command here is .ping (in discord)
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')    # when .ping is sent, bot returns 'Pong!'
"""
""" - BEFORE COGS *example* -
@client.command()    # turn on switch for command (discord)
async def broom(ctx):       # command here is .broom (in discord)
    await ctx.send('You\'re a wizard, Harry!')   # when .broom is sent, bot returns 'You're a wizard Harry!'
                                                   # ctx - context
"""

@client.command(aliases=['8ball', 'eightball'])     # FOR DISCORD --> command trigger is .8ball or .eightball
async def _8ball(ctx, *, question):                
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.']
    await ctx.send(f'Question: {question}?\nAnswer: {random.choice(responses)}')

'''/////ADMIN COMMANDS/////
---------------------------------------------------------------------
'''
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):        # amount - amount of messages to clear .clear #  <-- num you put deletes number of messages it clears      
    await ctx.channel.purge(limit=amount)    # .channel is where the command .clear was run in
                                              #  limit is how many messages going to purge, which is to the set amount(5)
                                              # purge() is a method in discord library

@client.command()           
@commands.has_permissions(kick_members=True)      ## members can only KICK others if they have this permission ##  
async def kick(ctx, member : discord.Member, *, reason=' '):  # command to kick member in discord; '*' means anything after '*' add on for the reason
    await member.kick(reason=reason)                          # kick() is a method in discord library
    await ctx.send(f'Kicked{member.mention}')
    if reason == ' ':
        await ctx.send(f'{member.mention} was kicked from the server.')
    elif reason == reason:
        await ctx.send(f'{member.mention} was kicked from the server.\nReason: {reason}')               

@client.command()       
@commands.has_permissions(ban_members=True)      ## members can only BAN others if they have this permission ##                                       
async def ban(ctx, member : discord.Member, *, reason=None):   # command to ban member in discord; discord.Member = an object
    await member.ban(reason=reason)                            # ban() is a method in discord library
    await ctx.send(f'Banned {member.mention}')
    if reason == ' ':
        await ctx.send(f'{member.mention} was banned from the server.\nNo specific reason.')
    elif reason == reason:
        await ctx.send(f'{member.mention} was banned from the server.\nReason: {reason}')

@client.command()
@commands.has_permissions(ban_members=True)     ## members can only UNBAN others if they have this permission ##
async def unban(ctx, *, member):                 # command to kick member in discord; unban() is a method in discord library
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')     # User#1234 --> 'User' is the name of member
                                                              # User#1234 --> '#1234' is the discriminator of member
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

def is_it_me(ctx):
    return ctx.author.id == 334183722763026433   # author id for only my user

@client.command()
@commands.check(is_it_me)                      # author id for my user, no one can use it other than me
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}') # ex. ->  cogs.example.py will look for cog in folder cogs
                                               # example.py is my test cog file in cogs folder
@client.command()
@commands.check(is_it_me)                      # author id for my user, no one can use it other than me
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}') # ex. ->  cogs.example.py will look for cog in folder cogs
                                               # example.py is my test cog file in cogs folder
@client.command()                            
@commands.check(is_it_me)                      # author id for my user, no one can use it other than me
async def reload(ctx, extension):              # reloads commands.py cog file with any updates while bot is still running
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'!Reload Finished!\nFILE: {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):     # filename is the string containing the name of each file, ex. example.py; loops through each .py file
        client.load_extension(f'cogs.{filename[:-3]}') # [:-3] splices off '.py' off of file name --> 'example.py' --> 'example'

# I will regenerate a new token each day
client.run('ODEwOTQ1OTM1ODk4NTc0ODQ5.YCrCQQ.PAB1H1n3W4YoBCd8ydGVUi66clk')