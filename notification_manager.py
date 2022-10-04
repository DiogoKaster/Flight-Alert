
class NotificationManager:
    def __init__(self):
        self.first_name = str(input("First Name: "))
        self.last_name = str(input("Last Name: "))
        self.first_email = str(input("Your email: "))
        self.second_email = str(input("Repeat your email, please: "))
        self.verify_emails(self.first_email, self.second_email)
        self.state = True

    def verify_emails(self, email1, email2):
        if email1 != email2:
            self.state = False
        else:
            pass
