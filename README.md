Sure, I've formatted your text to make it look cooler and more organized:

# Email Verification Script

This Python script provides a convenient way to automate the process of verifying accounts with email and extracting verification codes from emails sent by a specific source. It is designed to work with email accounts that are compatible with the `imaplib` library.

## Key Features

- **Email Verification**: The script logs into a user's specified email account, checks for new emails from the specific email address you provide, and extracts the verification code contained in the email subject.

- **Ease of Use**: Users can specify their email account credentials, including email address and password, in a text file (`credentials.txt`), making it easier to work with multiple email accounts within loops.

- **Code Extraction**: The script intelligently parses email subject lines to extract numeric verification codes, which can be used for various purposes, such as account verification on external platforms.

## Usage Instructions

1. Ensure that the necessary dependencies, including the `imaplib` library, are installed.

2. Add your email address and password with the following format in `credentials.txt`: `email_address,password`.

3. If you're only working with one email account, you can specify the line number in the text file that corresponds to your account. You can do this by calling the function as follows: `email_verify(line_number=1)`.

### Using Line Numbers for Multiple Accounts

When working with multiple email accounts within a loop, you need to use the `line_number` variable. By iterating through different line numbers in the `credentials.txt` file. You can achieve this by including the following code snippet inside your for loop:

```python
for email, password in credentials:
    email_verify(line_number)
    line_number += 1
```

**Note**: Ensure that your email account allows IMAP access.

By using this simplified script, users can easily retrieve verification codes from their email accounts, streamlining the process of confirming email addresses for various online services and applications.
