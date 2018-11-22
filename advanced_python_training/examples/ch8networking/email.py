import smtplib
import datetime

from email.mime.text import MIMEText
fp = open('textfile.txt', 'rb')
msg = MIMEText(fp.read())
fp.close()

me = 'adam@adam.com'
you = 'otherperson@person.com'
now = datetime.datetime.now()

msg['Subject'] = \
    'Contents'
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP('google smtp')
s.starttls()
s.login(me, open('password.txt').readline())
s.sendmail(me, [you], msg.as_string())
quit()
