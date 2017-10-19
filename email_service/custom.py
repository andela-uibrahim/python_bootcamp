from smtplib import SMTP, SMTPAuthenticationError, SMTPException

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
try:
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occured")

email_conn.quit()