from django.core.mail import send_mail
from RealEstate.settings import DEFAULT_FROM_EMAIL

def mail(email, username, password):
    message = f"""
    Account has been created
    Login details:
    Username: {username}
    Password: {password}
    Click to login: realestate.pythonanywhere.com
    """
    send_mail(
        'Account Created',
        message,
        DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )


def sendMail(email, subject, message):
    send_mail(
        subject,
        message,
        DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )


def multiMail(subject, message):
    file = open('emails.txt', 'r')
    mails = readlines(file)
    for i in mails:
        send_mail(
            subject,
            message,
            DEFAULT_FROM_EMAIL,
            [i],
            fail_silently=False,
        )
    file.close()
    reply = "All mails has been sent successfully"
    return reply


def writeMail(email):
    file = open('emails.txt', 'w')
    file.write(email)
    file.close()