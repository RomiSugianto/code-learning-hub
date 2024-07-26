import smtplib
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def send_email(config):
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = config['EMAIL']['from']
    msg['To'] = ', '.join(config['EMAIL']['to'].split(','))
    msg['Cc'] = ', '.join(config['EMAIL']['cc'].split(','))
    msg['Subject'] = config['EMAIL']['subject']

    # Attach the email body
    body = config['EMAIL']['body']
    msg.attach(MIMEText(body, 'plain'))

    # Convert recipient lists to a single list
    recipients = config['EMAIL']['to'].split(',') + config['EMAIL']['cc'].split(',')

    try:
        # Establish a secure session with the server
        server = smtplib.SMTP(config['SMTP']['smtp_server'], config['SMTP']['smtp_port'])
        server.starttls()
        server.login(config['SMTP']['username'], config['SMTP']['password'])

        # Send the email
        server.sendmail(config['EMAIL']['from'], recipients, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    config = load_config('config.ini')
    send_email(config)
