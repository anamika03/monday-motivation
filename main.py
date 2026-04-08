import smtplib
import datetime as dt
import random
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:  # Thursday is represented by 3
    with open("qoutes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() 
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs=MY_EMAIL, 
        msg=f"Subject:Monday Motivation\n\n{quote}"
    )
print("Email sent successfully!")

