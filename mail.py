import config
import smtplib
from contextlib import contextmanager

@contextmanager
def smtp_server():
    server = smtplib.SMTP(config.lookup("smtp.server"))
    def activate_tls():
        server.starttls()
    security = config.lookup("smtp.security")
    if security:
        {
            "tls": activate_tls,
        }[security]()
    username = config.lookup("smtp.username")
    password = config.lookup("smtp.password")
    server.login(username, password)
    yield server
    server.quit()

def send_message(message, recipient="default"):
    target = config.lookup(["recipients", recipient, "email"])
    sender = config.lookup("smtp.from") or config.lookup("smtp.username")
    with smtp_server() as server:
        server.sendmail(sender, target, message)

if __name__ == '__main__':
    import datetime
    import random
    message = """\
Subject: Here's a notification!

The time is now: {}
Here's a random number: {}
Have a nice day!
""".format(datetime.datetime.now(), random.random())
    print message
    send_message(message)
