import smtplib
import os


class Message:
    def __init__(self):
        self.my_email = "davidharket123@gmail.com"
        self.my_password = os.getenv("APP_PASSWORD")

    def send_self(self, email, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.my_email,
                msg=f"Subject: Melding Fra:\n\n"
                    f" Fra: {email}\n\n"
                    f" Melding: {message}".encode("utf-8")
            )
