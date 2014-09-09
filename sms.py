import config
from twilio.rest import TwilioRestClient

def send_message(text, recipient="default"):
    sid = config.lookup("twilio.sid")
    token = config.lookup("twilio.token")
    from_number = config.lookup("twilio.number")
    target = config.lookup(["recipients", recipient, "phone"])
    client = TwilioRestClient(sid, token)
    client.messages.create(body=text, to=target, from_=from_number)

if __name__ == '__main__':
    import sample
    sample.send_sample_message(send_message)
