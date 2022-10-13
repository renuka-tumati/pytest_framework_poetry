# content of emaillib.py
class MailAdminClient:
    def create_user(self):
        print("called create user")
        return MailUser()

    def delete_user(self, user):
        # do some cleanup
        print("called delete user")
        pass


class MailUser:
    def __init__(self):
        self.inbox = []

    def send_email(self, email, other):
        other.inbox.append(email)

    def clear_mailbox(self):
        self.inbox.clear()


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body