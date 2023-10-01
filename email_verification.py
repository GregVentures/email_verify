import imaplib
import email
from email.header import decode_header
import re


def email_verify(line_number):
    imap_server = 'outlook.office365.com'
    port = 993
    with open('credentials.txt', 'r') as file:
        lines = file.read().splitlines()
    if 0 <= line_number < len(lines):
        phone_number, email_address, password, credit_card, date, cvc, post, proxy = lines[line_number].split(',')
        print(f"Verifying email address: {email_address}")

        imap = imaplib.IMAP4_SSL(imap_server, port)
        imap.login(email_address, password)
        imap.select('Inbox')
        search_criteria = '(FROM "noreply@dice.fm")'
        result, email_ids = imap.search(None, search_criteria)

        if email_ids[0]:
            latest_email_id = email_ids[0].split()[-1]
            result, email_data = imap.fetch(latest_email_id, "(RFC822)")

            raw_email = email_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            subject, encoding = decode_header(email_message["Subject"])[0]
            email_body = ""

            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        email_body = part.get_payload(decode=True).decode(encoding or "utf-8")
            else:
                email_body = email_message.get_payload(decode=True).decode(encoding or "utf-8")

            subject = subject.decode('utf-8')
            code = re.sub("[^0-9]", "", subject)
            print(f"Verification code: {code} for email address: {email_address}")

            # print(f"No verification email found for email address: {email_address}")
        return code
    else:
        print("Invalid line number provided.")
        return None

email_verify(line_number=1)
