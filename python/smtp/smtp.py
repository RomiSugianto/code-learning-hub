import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email content
sender_email = "po@staging.farmindo.com"
receiver_email = "qc@staging.farmindo.com"
subject = "Test email"
message = "Hello, this is a test email!"

# SMTP server configuration
smtp_server = "10.10.11.50"
smtp_port = 587
smtp_username = "po@staging.farmindo.com"
smtp_password = "Paramadaksa123;"

# Create message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Send message
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")