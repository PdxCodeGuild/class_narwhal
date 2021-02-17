from __future__ import print_function
import datetime
import pickle
import os.path
from google import auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import arrow
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
PASSWORD = os.getenv('GOOGLE_PASSCODE') #password is stored in a .env file and since account has 2 factor auth the password is a google generated pass that includes the auth.
MY_EMAIL = os.getenv('EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')

#Sign in
def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    
    return service

# Call the Calendar API for events
def get_events(service):
    """
    Returns the selected number(n) of events on the user's calendar.
    """
    messages = []
    today = arrow.utcnow()
    start = today.floor('day')
    end = (today.ceil('day'))

    print(f'Getting the upcoming events')
    events_result = service.events().list(calendarId='primary', timeMin=start,
                                        timeMax=end,singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        message = {}
        start = event['start'].get('dateTime', event['start'].get('date'))
        message['Subject'] = event['summary']
        description = event['description'].split('\n')
        for each in description:
            each = each.split(': ')
            message[each[0]] = each[1]
        messages.append(message)
    return(messages)


service = authenticate_google()
messages = get_events(service)



