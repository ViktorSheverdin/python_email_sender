import smtplib
import credentials
import datetime as dt
import random
import time
import csv
import os

# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=credentials.sender_email,
#                      password=credentials.password)
#     connection.sendmail(
#         from_addr=credentials.sender_email,
#         to_addrs=credentials.recepient_email,
#         msg="Subject:Hello\n\nTHis is the body"
#     )


def main():
    while True:
        now = dt.datetime.now()
        friend_list = return_friend_list()
        for friend in friend_list:
            try:
                print("friend month: %s day: %s" % (friend[3], friend[4]))
                print(now.month)
                print(now.day)
                if now.month == int(friend[3]) and now.day == int(friend[4]):
                    # try:
                    print("Sending Happy bday")
                    send_happy_bday(friend)
            except IndexError:
                print("Out of range")
        time.sleep(86400)


def return_friend_list():
    birthdays_file = "birthdays.csv"
    friend_list = []
    with open(birthdays_file, "r") as bdays:
        csvreader = csv.reader(bdays)
        for row in csvreader:
            friend_list.append(row)
    bdays.close()
    return friend_list


def return_email_body():
    files = []
    for file in os.listdir("./letter_templates"):
        files.append(file)
    with open(f"./letter_templates/{random.choice(files)}", "r") as email_template:
        return email_template.read()


def send_happy_bday(friend):
    email_body = return_email_body()
    email_body = email_body.replace("[NAME]", friend[0], 1)
    # print(email_body)
    # print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=credentials.sender_email,
                         password=credentials.password)
        connection.sendmail(
            from_addr=credentials.sender_email,
            to_addrs=credentials.recepient_email,
            msg=f"Subject:Happy Birthday!\n\n{email_body}"
        )


# def return_quote():
#     with open("quotes.txt", "r") as file:
#         quotes = file.readlines()
#         random_quote = random.choice(quotes)
#         print(random_quote)
#         return return_quote


main()
