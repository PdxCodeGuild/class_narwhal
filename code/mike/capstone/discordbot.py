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

def get_lottery():
    lottery = []
    for num in range(5):
        num = random.randint(1,69)
        lottery.append(num)
    bonus = random.randint(1,26)
    lottery.append(bonus)
    return lottery

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
    if message.content.startswith('hello'):
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



client.run(token)
