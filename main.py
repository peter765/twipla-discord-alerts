from webhook_client import WebhookClient
from twipla_event import TwiplaEvent
import time
import os

tsunagaru_day_1 = {
        'name':'Tsunagaru Mirai Day 1',
        'twipla_url':'https://twipla.jp/events/336075',
        #'avatar_url': '' #optional
    }

tsunagaru_day_2 = {
        'name':'Tsunagaru Mirai Day 2',
        'twipla_url':'https://twipla.jp/events/370681',
        #'avatar_url': '' #optional
    }

tsunagaru_day_3 = {
        'name':'Tsunagaru Mirai Day 3',
        'twipla_url':'https://twipla.jp/events/382544',
        #'avatar_url': '' #optional
}


events = [
    TwiplaEvent(params=tsunagaru_day_1), 
    TwiplaEvent(params=tsunagaru_day_2), 
    TwiplaEvent(params=tsunagaru_day_3)
    ]
client = WebhookClient(os.environ["WEBHOOK_URL"])

# create state variables to not duplicate announcements
num_slots = [-1 for _ in range(len(events))]

while(1):

    for i, event in enumerate(events):
        attending, total, remaining = event.get_status()
        print(event.params['name'])
        if num_slots[i] != remaining: #if the number of taken slots change, send channel message
            num_slots[i] = remaining
            # alert the change in the channel
            event.alert_channel(client)
    print("waiting")
    time.sleep(30)