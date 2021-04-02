import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils import config

def sendEmailViaGmailSMPT(senderEmailAddress,senderPassword,receiversEmailAddresses, body):

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(senderEmailAddress, senderPassword)
    server.sendmail(senderEmailAddress, receiversEmailAddresses, body)
    server.quit()
    return

counter = 0
minutes_per_day = 24 * 60

while(True):
    counter += 1

    for doctor in config.doctorCodes.keys():
        url = config.baseURL + str(config.doctorCodes[doctor])
        r = requests.get(url)
        if r.text.find("Disponibile") != -1:
            message = "Doctor {} is available".format(doctor)

            msg= MIMEMultipart('alternative')
            msg['Subject'] = config.subject
            msg['From'] = config.senderEmailAddress
            msg['To'] = config.receiver
            partText = MIMEText(message, 'plain')
            msg.attach(partText)

            print("Doctor {} is avaliable. Sending mail to {}".format(doctor, config.receiver))
            sendEmailViaGmailSMPT(config.senderEmailAddress, config.senderPassword, config.receiver, msg.as_string())
        else:
            print("Doctor {} is not available".format(doctor))

    if counter == minutes_per_day/config.sleepMinutes:
        counter = 0
        message = "Test message"

        msg= MIMEMultipart('alternative')
        msg['Subject'] = "Test Doctor Availability"
        msg['From'] = config.senderEmailAddress
        msg['To'] = config.receiver
        partText = MIMEText(message, 'plain')
        msg.attach(partText)

        print("Sending test message")
        sendEmailViaGmailSMPT(config.senderEmailAddress, config.senderPassword, config.receiver, msg.as_string())      
    time.sleep(config.sleepMinutes * 60)
