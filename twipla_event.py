import requests
import re

class TwiplaEvent():
    default_params = {
        'name':'',
        'twipla_url':'',
        #'avatar_url': '' #optional
    }

    """
    Class for creating a TwiplaEvent
    """
    def __init__(self, params=default_params):
        self.params = params
        self.attending = 0
        self.total = 0

    
    def __str__(self):
        print(self.params.name)
    
    def get_status(self):
        '''
        parse twipla page to get openings
        returns occupied, total, and remaining available
        '''
        self.update_status()
        return self.attending, self.total, (self.total - self.attending)

    def alert_channel(self, webhookclient):
        '''
        sends message to channel specified in webhook client
        '''
        username = self.params['name'] + " Status"
        remaining_slots = self.total - self.attending

        if remaining_slots != 0:
            message = "{} has **{}** slots remaining out of {}!".format(self.params['name'], 
                remaining_slots, self.total)
            color = 39423
        else :
            message = "This event is now full. Keep checking!"
            color = 16711680
        
        #use discord embed syntax, needs work
        # msg_data = {
        #     'username': username,
        #     'embeds': [
        #         {
        #             'title': message,
        #             'url': self.params['twipla_url'],
        #             'color': color
        #         }
        #     ]
        # }
        msg_data = {
            'username': username,
            'content': message,
        }

        webhookclient.send_message(msg_data) #send message via webhook client

    def update_status(self):
        '''
        parse twipla page to get openings
        updates self.attending, self.total
        ''' 
        twipla_url = self.params['twipla_url']
        print(twipla_url)


        
        # request the webpage html text
        resp = requests.get(twipla_url, verify=False).text

        try:
            # use regex to find the attending and total
            regex = r"参加者 \(([0-9]+)人／定員([0-9]+)人\)"
            match = re.search(regex, resp, re.MULTILINE)
            self.attending = int(match.group(1))
            self.total = int(match.group(2))
        except Exception:
            print("Unable to match regex")
            print(twipla_url)
            self.attending=0
            self.total=0

        print(self.attending)
        print(self.total)



    