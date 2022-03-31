import random
import smtplib
import datetime

my_email = "khashstudioz@gmail.com"
password = "Hash@123"

week_days = ['Monday',"Tuesday", "Wednesday","Thursday", "Friday","Saturday", "Sunday"]

now = datetime.datetime.now()
# print(now.day)
# print(now.month)
# print(now.year)
day = week_days[now.weekday()]

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()         #Return all lines in the file, as a list where each line is an item in the list object
    quote = random.choice(all_quotes)
print(quote)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()                       # securing our connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="kanishka@hashstudioz.com",
        msg=f"Subject:{day} Motivation\n\n{quote}."
    )
    print("mail sent")