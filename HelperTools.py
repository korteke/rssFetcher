# -*- coding: utf-8 -*-
# Author Keijo Korte / 25.08.2016

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
sender = "blop@blop.com"
receiver = "noc@blop.com"

def notifyAdmins(message):
    ''' Sends email to the admins if something strange happends when fetching rss-feed '''
    '''
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "RssFetcher cant fetch"
 
    body = str(message).encode('utf-8').strip()
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()
    '''
    print "Sending email"
