import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = ""
recipient_email = ""
password = ""

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = "Test Email From Python"

body = "Hello! This is you"
message.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.login(sender_email, password)

    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email Sent Successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    server.quit()


from email.mime.base import MIMEBase
from email import encoders

filename = "Files/read_example.csv"
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

message.attach(part)