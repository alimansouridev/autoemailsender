from email.message import EmailMessage
import ssl
import csv
import smtplib
import conem
from conem import email_body


# Enter Your Email
emailsender = ""

# Enter Your Email Password
email_password = ""

email_receiver = ""

# Enter Subject
subject = ""
body = email_body

em = EmailMessage()

em["From"] = emailsender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

# Python program to read CSV file line by line
# import necessary packages
# Open file
with open("email.csv") as file_obj:
    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)
    # Iterate over each row in the csv
    # file using reader object
    for row in reader_obj:
        ma = row[0]
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(emailsender, email_password)
            smtp.sendmail(emailsender, ma, em.as_string())
