import smtplib
import credentials
import datetime as dt
import random
import time

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
        if now.weekday() == 5 and now.hour == 18 and now.minute == 37:
            send_quote()
            time.sleep(61)


def send_quote():
    quote = return_quote()
    # print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=credentials.sender_email,
                         password=credentials.password)
        connection.sendmail(
            from_addr=credentials.sender_email,
            to_addrs=credentials.recepient_email,
            msg=f"Subject:Motivational quote\n\n{quote}"
        )


def return_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
        print(random_quote)
        return return_quote


main()
