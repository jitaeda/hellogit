import os.path

from smtplib import SMTP

from email.mime.text import MIMEText

from email.mime.application import MIMEApplication

from email.mime.multipart import MIMEMultipart

def send_mail(from_addr, to_addr, subject, content, files=[]):
    content_type = "html"
    username = 'jitaeda1@gmail.com'
    password = 'nmralkperffegfhl'
    smtp = 'smtp.gmail.com'
    port = 587
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg.attach(MIMEText(content, content_type))
    if files:
        for f in files:
            with open(f, 'rb') as a_file:
                basename = os.path.basename(f)
                part = MIMEApplication(a_file.read(), Name=basename)

                part['Content-Disposition'] = 'attachment; filename="%s"' % basename
                msg.attach(part)
    mail = SMTP(smtp)
    mail.ehlo()
    mail.starttls()
    mail.login(username, password)
    mail.sendmail(from_addr, to_addr, msg.as_string())
    mail.quit()