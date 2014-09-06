What is this?
=============

It's a Python module to allow you to easily send messages to yourself.
It's meant to serve as a notification module for other scripts, to
allow them to share both the code to send messages by various
mechanisms, and the configuration file which determines both where
those messages go and where they are sent from (including credentials
to send).

Currently the module supports only notification via SMTP (e.g. sending
from a GMail account).

How do I use it?
================

Prerequisites:

 - You must have the module accessible in your `PYTHONPATH`
 - You must have created a suitable configuration file (see below)

The following code should then suffice in a script which wishes to
send a notification:

    import notify.mail
    notify.mail.send_message("Hello world!")

Configuration file
==================

The configuration file is a YAML file which should usually be located
at `~/.notify.yaml`.

The configuration file serves two purposes:

  - It stores your means of sending messages, and the associated credentials.
  - It stores the recipient addresses where you would like to receive messages.

See `notify.example.yaml` for a sample configuration file.

Remember that the configuration file contains secret information, e.g.
passwords to your email accounts in plaintext. Take appropriate precautions:

 - If you are on a multi-user system, remember to set the permissions to the
   file appropriately (e.g. `chmod 600`).
 - Be mindful of any backups made that include the configuration file.
 - **Never commit the configuration file to a public source code repository!**

Security considerations
=======================

On general principle it is advisable to isolate the credentials you use for
notification.

Specifically, don't use a general-purpose email account to send notifications.
Instead, create a new email account that you will use only for this purpose.

This minimizes the impact of any possible leak (e.g. through inappropriate
handling of file permissions).
