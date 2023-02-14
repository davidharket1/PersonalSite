import smtplib
import os

class Message:
    def __init__(self):
        self.my_email = "davidharket123@gmail.com"
        self.my_password = os.getenv("APP_PASSWORD")

    def send_self(self, email, days, date, address, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.my_email,
                msg=f"Subject: Melding Fra:\n\n"
                    f" E-post: {email}\n\n"
                    f" Leielengde: {days}\n"
                    f" Fra denne datoen: {date}\n"
                    f" Til denne addressen: {address}\n"
                    f" Ekstra beskjed: {message}".encode("utf-8")
            )

    def send_cus(self, email, days, date, address, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=f"{email}",
                msg=f"Subject: Takk for din bestilling!:\n\n"
                    f"En kundebehandler kontakter deg straks.\n\n"
                    f"Informasjon om bestillingen\n"
                    f"Antall dager: {days}\n"
                    f"Fra denne datoen: {date}\n"
                    f"Til denne addressen: {address}\n"
                    f"Ekstra beskjed:{message}\n".encode("utf-8")
            )
