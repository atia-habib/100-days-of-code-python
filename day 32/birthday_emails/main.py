import smtplib
import pandas as pd
import datetime as dt
import random

# Read the CSV file
data = pd.read_csv("birthdays.csv")

# Email credentials
my_email = "atiahabib48@gmail.com"
my_password = "clqenibxelquzwbh"

# Get today's date
now = dt.datetime.now()
today = (now.month, now.day)

# Create a dictionary from the CSV (key: (month, day), value: row)
birthdays_dict = {(row["month"], row["day"]): row for _, row in data.iterrows()}

# Check if today's date is in the dictionary
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person["name"]
    email = birthday_person["email"]

    # Pick a random letter template
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"  # Assuming you have letter_1.txt, letter_2.txt, letter_3.txt
    with open(letter_path) as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content.replace("[NAME]", name)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{letter_content}",
        )

    print(f"Birthday email sent to {name} at {email}!")
else:
    print("No birthdays today.")
