import sys

from celery import shared_task
from django.core.mail import send_mail
from django4.settings import EMAIL_HOST_USER
from bs4 import BeautifulSoup
import requests
from .models import Author, Quotes
import time


@shared_task
def send_mail_to(subject, message, receivers):
    send_mail(subject, message, EMAIL_HOST_USER, [receivers])


@shared_task
def quotes():
    a = time.time()
    page = 1
    p = 0
    while p < 5:
        url = f'https://quotes.toscrape.com/page/{page}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')
        sys.stdout.write(f'IN {url}: {page}')
        if not soup.find_all('li', class_='next'):
            p = 5
            send_mail_to('Quotes Task!', 'There are not new quotes.', 'admin@admin.com')

        quo = soup.find_all('div', class_='quote')

        for i in quo:
            url2 = 'https://quotes.toscrape.com'+i.find('a').get('href')
            response2 = requests.get(url2)
            i2 = BeautifulSoup(response2.text, features='html.parser')
            text = i.find('span', class_='text').text
            author = i.find('small', class_='author').text
            born_date = i2.find('span', class_='author-born-date').string
            born_location = i2.find('span', class_='author-born-location').string
            description_text = i2.find('div', class_='author-description').string

            if not Quotes.objects.filter(quotes=text).exists():
                Quotes.objects.create(quotes=text,
                                      author=Author.objects.get_or_create(name=author,
                                                                          born_info=born_date+born_location,
                                                                          description=description_text)[0])
                p += 1
                if p == 5:
                    break
                sys.stdout.write(f'QUOTE     {p}')

        page += 1
        sys.stdout.write(f'OUT {page}')
        sys.stdout.write(f'QUOTES    {p}')
    sys.stdout.write(str(time.time()-a))
