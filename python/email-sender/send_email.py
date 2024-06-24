import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# SMTP server credentials
smtp_server = 'webmail.nexcloud.id'
smtp_port = 587  # Update with your SMTP server port
smtp_username = 'test@farmindo.net'
smtp_password = '!Test123'

# Sender email address
sender_email = 'test@farmindo.net'

# Read the list of recipient emails from a file
with open('recipient_emails.txt', 'r', encoding="utf-8") as file:
    recipient_emails = [line.strip() for line in file]

# Email content
subject = 'Your Subject'
body = 'Your email body goes here with <img src="cid:image.jpg"> for inline image.'
attachment_path = 'image.jpg'

# Create the MIME object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = subject

# Add body text
msg.attach(MIMEText(body, 'html'))

# Add inline image
with open(attachment_path, 'rb') as file:
    img = MIMEImage(file.read(), name='image.jpg')
    img.add_header('Content-ID', '<image1>')
    msg.attach(img)

# Attach the file
attachment = open(attachment_path, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % 'image.jpg')
msg.attach(part)

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email to each recipient using BCC
    for recipient in recipient_emails:
        msg['To'] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())

print("Emails sent successfully.")
