def send_sample_message(f, **kwargs):
    import datetime
    import random
    message = """\
The time is now: {}
Here's a random number: {}
Have a great day!
""".format(datetime.datetime.now(), random.random())
    print message
    f(message, **kwargs)
