#~~~ Pratham-code ~~~
# import
import os
from email.message import EmailMessage
import ssl
import smtplib
from getpass import getpass
import time

# mail password
send = 'tastpro28@gmail.com'

password = 'muuyaircfwqhifgm'
receiver ='patelpratham281@gmail.com'

# body
subject ="testing python mailsend"
body = """
 bot is online i am python
"""
em = EmailMessage()
em['From🤖'] = send
em['to'] = receiver
em['Subject'] = subject
em.set_content(body)

contest = ssl.create_default_context()

# main code
print("login")
A1 = input("user\n")
if A1 == 'Pratham':
    A2 = getpass("password\n")
    if A2 == '2806':
      time.sleep(5)
      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contest) as smtp:
          smtp.login(send, password)
          smtp.sendmail(send, receiver, em.as_string())
      print("send")

    else:
        print("not found")
else:
    print("not found")

#~~ MAINCODE ~~
print("bot in run")
time.sleep(5)

msend2()