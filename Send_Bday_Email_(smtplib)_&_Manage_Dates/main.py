##################### Extra Hard Starting Project ######################
import datetime
import pandas
import random
import smtplib


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row['month'], data_row['day']): data_row for(index, data_row) in data.iterrows()}



my_email = "khashstudioz@gmail.com"
password = "Hash@123"

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.


today = datetime.datetime.now()
today_tuple = (today.month, today.day)
print(today_tuple)

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    num = random.randint(1,3)
    file_path = f"letter_templates/letter_{num}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:                     # 587 is default mail submission port
        connection.starttls()                       # securing our connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= bday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{contents}."
        )
    print("mail sent")



""" To run this code everyday :
    signup on 'pythonanywhere.com' > files > upload files > consoles > Bash > Type 'python3 main.py' > 
    (now schedule a task to run it everyday) Tasks > schedule your time according to UTC and type same command (python3 main.py) 
    at UTC section """

""" Note : now this code will run everyday at your selected time """