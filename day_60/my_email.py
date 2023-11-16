import smtplib

def send_email(reciver , pas):
    send = "rehansnehalshah1@gmail.com"
    message = f"Thank you for regestration , please not your password , It is {pas}"
    password = "aqsynzrwxmrtqcju"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=send, password=password)
        connection.sendmail(
            from_addr=send,
            to_addrs=reciver,
            msg=message
        )
