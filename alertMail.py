import os
import shutil
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def sendMail(toaddr,attachments):
    fromaddr = "noreply.homesurveillance@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "[HomeSurveillance] Unknow Person Detected"
    body = "Unknown person detected in premises at "+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+"\n Please find attached images of the person."

    msg.attach(MIMEText(body, 'plain'))


    for attachment in attachments:
        filename = attachment.split("\\")[-1]
        attachment = open("temp/"+attachment, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, "home_surveillance#Gmail")

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

    # shutil.rmtree("temp")
    # os.mkdir("temp")
    print("====================================================================")
    print("====================================================================")
    print("Mail sent")
    print("====================================================================")
    print("====================================================================")
    return True
