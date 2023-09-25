from .models import Student
import time
from django.core.mail import send_mail

from django.conf import settings


def a():
    print("fuc sorted")
    time.sleep(1)
    print("executed")


def send_email_to_client():
    subject="this dj"
    message="hii"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["mishradipti2402@gmail.com"]

    send_mail(subject,message,from_email,recipient_list)
