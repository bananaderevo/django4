from celery import shared_task
from django.core.mail import send_mail
from django4.settings import EMAIL_HOST_USER
from bs4 import BeautifulSoup
import requests
from .models import *
import time
import re


@shared_task
def send_mail_to(subject, message, receivers):
    send_mail(subject, message, EMAIL_HOST_USER, [receivers])


@shared_task
def quotes():
    a = time.time()
    o = 1
    p = 0

    while p != 1:
        url = f'https://quotes.toscrape.com/page/{o}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')
        quo2 = soup.find_all('li', class_='next')
        # link = soup.find('div', class_='quote').a
        # print(link['href'])
        # # print(re.findall(r'""(.*?)""', str(link)))
        # p = 1
        print(f'IN {url}: ', o)
        if not quo2:
            p = 1

        quo1 = soup.find_all('span', class_='text')
        quo = soup.find_all('div', class_='quote')

        for i in quo:
            text = i.find('span', class_='text').text
            author = i.find('small', class_='author').text
            if not Quotes.objects.filter(quotes=text).exists():
                Quotes.objects.create(quotes=text).author.set(Author.objects.get_or_create(name=author))
            # if not Author.objects.filter(name=author.text).exists():
            #     link = soup.find('div', class_='quote').a['href']
            #     soup2 = BeautifulSoup(requests.get(f'https://quotes.toscrape.com/{link}').text, features='html.parser')
            #     Author.objects.create(name=author.text,
            #                           born_info=soup.find('span', class_='author-born-date') + soup.find('span', class_='author-born-location'),
            #                           description=soup.find('div', class_='author-description'))
            #     Quotes.objects.create(quotes=text.text).author=Author.objects.last()
            # elif Author.objects.filter(name=author.text).exists() and Quotes.objects.filter(quotes=text.text).exists() == False:
            #     Quotes.objects.create(quotes=)
        o += 1
        print('OUT ', o)
    print(time.time()-a)
