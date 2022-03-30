"""  specify your location of server provider acc to your mail; the protocol for mail submission actually uses 587 """


""" TLS stands for transport layer security, its a way of securing our connection to our email server,
    so that way, when we're sending an email and if somebody else intercepts our email somewhere along the line and
    they try to read it, because this is enabled, that message will be encrypted and it will be impossible for them to
    read our email """

""" by default gmail doesn't allow anyone to access your email account; and in order to send email from ur gmail
using python you need to lower the security boundaries :

    1) manage your google accounts
    2) security
    3) make sure your signing to google section is turned off (use ur phn to sign in and 2-step verification
    4) turn on the less secure app access"""

""" message will be sent to the spam box"""