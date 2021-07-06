from celery import shared_task
from django.core.mail import send_mail
from django4.settings import EMAIL_HOST_USER
from bs4 import BeautifulSoup
import requests


url = 'https://quotes.toscrape.com/'

@shared_task
def send_mail_to(subject, message, receivers):
    send_mail(subject, message, EMAIL_HOST_USER, [receivers])


# @shared_task
# def quotes():
#     page = requests.get(url)
#     print(page.status_code)