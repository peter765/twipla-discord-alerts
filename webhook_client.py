import requests

class WebhookClient():

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        print('Starting Webhook with url ' + webhook_url)

    
    def send_message(self, data):
        r = requests.post(self.webhook_url, data, verify=False)




