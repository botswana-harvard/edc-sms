import urllib


class SendMessage:

    def send(self, message_data=None, recipient_number=None):
        url = (
            'https://sms.mobilenterprises.com:9443/api?action=sendmessage&'
            f'username=BHP&password=21K50uShD&recipient={recipient_number}&'
            f'messagetype=SMS:TEXT&messagedata={message_data}')
        req = urllib.request.Request(url)
        urllib.request.urlopen(req)
