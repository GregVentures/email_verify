# email_verify
This Python script provides a convenient way to automate the process of verifying accounts with email and extracting verification codes from emails sent by a specific source.
It is designed to work with email accounts that works with the imaplib libary.

Key Features:

Email Verification: The script logs into a user's specified email account, checks for new emails from the specific email adress you provide and extracts the verification code contained in the email subject.

Ease of Use: Users can specify their email account credentials, including email address and password, in a text file (credentials.txt) therefor making it easier to work with multible email accounts within loops.

Code Extraction: The script intelligently parses email subject lines to extract numeric verification codes, which can be used for various purposes, such as account verification on external platforms.

Usage Instructions:

1. Ensure that the necessary dependencies, including the imaplib library, are installed.

2. Create a text file named credentials.txt with the following format: email_address,password

3. if ur only working with one email account you need to specify what line in the txt your account is on. You can just do this by calling the function in the following way: email_verify(line_number=1)

Using Line Numbers for Multiple Accounts:

When working with multiple email accounts within a loop, you need to use the line_number variable. By iterating through different line numbers in the credentials.txt file.
You do this by writing th following variable inside ur for loop: line_number += 1
An example os using this in a for loop could be:

for email, password in credentials:
    login_to_reddit(email, password)
    line_number += 1


Note: Ensure that your email account allows IMAP access.

By using this simplified script, users can easily retrieve verification codes from their email accounts, streamlining the process of confirming email addresses for various online services and applications.







