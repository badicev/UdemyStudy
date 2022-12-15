# import smtplib
#
# my_email = "basakdilaracevik4@gmail.com"
# password = "Placeholder"  # gmail 2-step verification password's app
#
# with smtplib.SMTP("smtp.gmail.com")  as connection: # Simple Mail Transfer Protocol (SMTP)
#     connection.starttls()  # Transport Layer Security (TLS)
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="cevikbasakdilara@gmail.com",
#         msg="Subject:Hello\n\n This is the "
#             "body of my email.")
#     connection.close()

import datetime as dt

now = dt.datetime.now()
print(now)