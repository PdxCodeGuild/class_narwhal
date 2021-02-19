'''
First attempt at making a discord bot.
Random Bot will return random information based on commands.
'''

# import discord and os libaries
import discord
import os
import json
import requests
import random
from datetime import date

# create client to connect to discord
client = discord.Client()
token = os.getenv('TOKEN')

# random facts using Random Uselsess Facts REST API v1.0 by https://jsph.pl
def get_fact():
    response = requests.get(f'https://uselessfacts.jsph.pl/random.json?language=en')
    json_data = json.loads(response.text)
    fact = json_data['text']
    return(fact)

# returns events that occurred on this day from wikipedia.org
def get_day():
    today = date.today()
    today = (f'{today.month}/{today.day}')
    response = requests.get(f'https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{today}')
    json_data = json.loads(response.text)
    random_event = random.choice(json_data['events'])
    day = 'In the year ' + str(random_event['year']) + ', ' + random_event['text']
    return day

# generate random 6 digit lottery number
def get_lottery():
    lottery = []
    for num in range(5):
        num = random.randint(1,69)
        lottery.append(num)
    bonus = random.randint(1,26)
    lottery.append(bonus)
    return lottery

# fuction to pull call of duty user stats
def cod_stats():
    platform = input('What platform is the user? (pc/ps4/xbox): ').lower()
    username = input('Enter Call of Duty Username: ')
    if platform == 'pc':
        username = username.replace('#', '%23')
    stats = f'https://codstats.net/warzone/profile/{platform}/{username}'
    return stats

# event callback function makes bot ready for use
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# event responding to message received and ignores message sent from self
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # calls get_fact definition to send random fact in discord
    if message.content.startswith('!!fact'):
        fact = get_fact()
        await message.channel.send(f'{message.author.name}, did you know {fact}')
        # removes message calling for random fact
        await message.delete()
    
    # bot responds with hello (user's name) when user says hello
    if message.content.startswith('!!hello'):
        await message.channel.send(f'Hello, {message.author.name}')

    # bot responds with 6 lottery numbers
    if message.content.startswith('!!lottery'):
        lottery = get_lottery()
        await message.channel.send(f'{message.author.name}, here are your lottery numbers! \n {lottery}')
        await message.delete()

    # bot returns today's date
    if message.content.startswith('!!date'):
        today = date.today()
        today = today.strftime('%B %d, %Y')
        await message.channel.send(f'{message.author.name}, today is {today}')

    # bot returns on this day
    if message.content.startswith('!!day'):
        day = get_day()
        await message.channel.send(f'On this day:{day}')
        await message.delete()

    # bot dances
    if message.content.startswith('!!dance'):
        await message.channel.send('https://tenor.com/view/happy-dancing-celebrate-excited-gif-13870839')
        await message.delete()

    # gets link to call of duty player stats
    if message.content.startswith('!!codstats'):
        stats = cod_stats()
        await message.channel.send(stats)

    # list available commands
    if message.content.startswith('!!help'):
        commands_help ='''
!!fact - Returns random fact
!!hello - Returns hello
!!lottery - Returns 6 Lottery Numbers
!!date - Returns today\'s date
!!day - Returns historical event that occured on today\'s date
!!dance - Makes bot dance
'''
        await message.channel.send(commands_help)
        await message.delete()

    # refers to !!help command
    if message.content.startswith('zant'):
        await message.channel.send('For Zant Bot Commands, type !!help')


client.run(token)

