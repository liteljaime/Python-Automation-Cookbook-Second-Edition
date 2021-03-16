import argparse
import configparser

import smtplib
from email.message import EmailMessage


def main(to_email, server, port, from_email, password):
    print(f'With 💜 from {from_email} to {to_email}')

    subject = 'With 💜'
    text = '''This is a test'''
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    server = smtplib.SMTP_SSL(server, port)
    # server.ehlo()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str, help='destination email')
    parser.add_argument(
        '-c', dest='config', type=argparse.FileType('r'), help='config file', default=None)

    args = parser.parse_args()

    if not args.config:
        print('Error, config file is required')
        parser.print_help()
        exit(1)

    config = configparser.ConfigParser()
    config.read_file(args.config)

    try:
        main(args.email, server=config['DEFAULT']['server'], port=config['DEFAULT']['port'],
             from_email=config['DEFAULT']['email'], password=config['DEFAULT']['password'])
    except:
        print('Something went wrong 😣😥')
