from datetime import date
import requests
import json
import random


# returns events that occurred on this day
def get_day():
    today = date.today()
    day = str(today.day)
    month = str(today.month)
    today = (f'{today.month}/{today.day}')
    response = requests.get(f'https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{today}')
    json_data = json.loads(response.text)
    random_event = random.choice(json_data['events'])
    day = str(random_event['year']) + ' - ' + random_event['text']
    return day


print(get_day())


