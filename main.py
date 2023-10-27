import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def sendEmailViaGmailSMPT(senderEmailAddress,senderPassword,receiversEmailAddresses, body):

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(senderEmailAddress, senderPassword)
    server.sendmail(senderEmailAddress, receiversEmailAddresses, body)
    server.quit()
    return


counter = 0
minutes_per_day = 24 * 60

with open("config.json") as json_conf:
    conf = json.load(json_conf)

    print("Starting main loop..")
    while(True):
        # Sleep at the beginning of the loop since if the program crashes due to a network error, for example, the container is restarted and it would
        # immediately experience the same crash. In this way if the program is restarted we wait sleepMinutes minutes before retrying again.
        time.sleep(conf["sleepMinutes"] * 60)
        counter += 1
        with open("doctors.json") as json_doctors:
            doctors = json.load(json_doctors)

            for doctorKey in doctors["doctors"].keys():
                doctor = doctors["doctors"][doctorKey]

                url = conf["baseURL"] + str(doctor["code"])
                r = requests.get(url)
                if r.text.find("Disponibile") != -1:
                    message = "Doctor {} is available".format(doctorKey)

                    msg= MIMEMultipart('alternative')
                    msg['Subject'] = conf["subject"]
                    msg['From'] = conf["senderEmailAddress"]
                    partText = MIMEText(message, 'plain')
                    msg.attach(partText)

                    msg['To'] = ", ".join(doctor["receiverEmail"])
                    print("Doctor {} is avaliable. Sending mail to {}".format(doctorKey, doctor["receiverEmail"]))
                    sendEmailViaGmailSMPT(conf["senderEmailAddress"], conf["senderPassword"], doctor["receiverEmail"], msg.as_string())
                else:
                    print("Doctor {} is not available".format(doctorKey))

            if counter == minutes_per_day/conf["sleepMinutes"]:
                counter = 0
                message = "Test message"

                msg= MIMEMultipart('alternative')
                msg['Subject'] = "Test Doctor Availability"
                msg['From'] = conf["senderEmailAddress"]
                msg['To'] = conf["adminEmail"]
                partText = MIMEText(message, 'plain')
                msg.attach(partText)

                print("Sending test message")
                sendEmailViaGmailSMPT(conf["senderEmailAddress"], conf["senderPassword"], conf["adminEmail"], msg.as_string())      
