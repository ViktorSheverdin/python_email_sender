import smtplib
import credentials

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=credentials.sender_email,
                     password=credentials.password)
    connection.sendmail(
        from_addr=credentials.sender_email,
        to_addrs=credentials.recepient_email,
        msg="Subject:Hello\n\nTHis is the body"
    )
