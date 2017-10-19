from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "geekydev043@gmail.com"
password = "Kratus043"
from_email = username

# list of users to send the mail
to_list = ["fantacylove007@gmail.com", "geekydev043@gmail.com"]


email_conn = SMTP(host, port)

# hand shaking with the email server
email_conn.ehlo()

# start secured layer for email encryption
email_conn.starttls()

the_msg = MIMEMultipart("alternative")
the_msg["Subject"] = "I Am a Boss"
the_msg["From"] = from_email

plain_txt = "Testing the Message"
html_text = """\
<html>
    <head></head>
    <body>
        <p> Hey! <br>
            Testing this email <b>message</b> made by <a href="fiverr.com/ammehy"> freemile baba </a> 
        </p>
    </body>
</html>
"""

part_1 = MIMEText(plain_txt, "plain")
part_2 = MIMEText(html_text, "html")

the_msg.attach(part_1)
the_msg.attach(part_2)

try:
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occured")

email_conn.quit()