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

def has_email_headers(message, require=("Subject")):
    lines = message.splitlines()
    try:
        header_terminator_index = lines.index("")
    except ValueError:
        return False
    headers = lines[:header_terminator_index]
    unmet = set(require)
    for header in headers:
        if ":" not in header:
            return False
        next_unmet = set()
        for req in unmet:
            if req not in header:
                next_unmet.add(req)
        unmet = next_unmet
    return not unmet

def format_email_headers(headers):
    return "".join(["{}: {}\n".format(k,v) for k, v in headers.items()])

def emailify(message):
    if has_email_headers(message):
        return message
    first_line = message.splitlines()[0]
    subject = first_line[:60]
    if subject != first_line:
        subject += "..."
    headers = {
        "Subject": subject
    }
    return "\n".join([format_email_headers(headers), message])

def send_message(message, recipient="default"):
    target = config.lookup(["recipients", recipient, "email"])
    sender = config.lookup("smtp.from") or config.lookup("smtp.username")
    message = emailify(message)
    with smtp_server() as server:
        server.sendmail(sender, target, message)

if __name__ == '__main__':
    import sample
    sample.send_sample_message(send_message)
