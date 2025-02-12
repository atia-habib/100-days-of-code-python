import smtplib
import datetime as dt
import random

my_email = "atiahabib48@gmail.com"
password = "clqenibxelquzwbh"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ahday32@yahoo.com",
            msg=f"Subject: Good morning quotes\n\n{quote} ",
        )

    # clqe nibx elqu zwbh
