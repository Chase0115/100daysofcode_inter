import smtplib

my_email = "smtppythontest.sample@gmail.com"
password = "qrpqrp0101"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="sgh0115@gmail.com",
        msg="Subject:Hello\n\n This is the body of my email.")
    connection.close()

