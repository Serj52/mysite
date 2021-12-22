import os, sys

import pytz
from pytz import UTC

sys.path.append(r'C:\Users\tcyganov_sa\PycharmProjects\untitled6\mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
from django.db.models import Q, Count, Avg, Sum
django.setup()
from datetime import date


from myapp.models import Producer, Festival, Category, Films, Recom


def create_producer(name, country, age):
    Producer.objects.create(name=name, country=country, age = age)

def create_festival(name, year):
    Festival.objects.create(name=name, year=year)

def create_category(name):
    Category.objects.create(name=name)

def create_films(name, year, genre, cat, fest, prod):
    c = Category.objects.get(name=cat)
    p = Producer.objects.get(name=prod)

    if fest != None:
        f = Festival.objects.get(name=fest)
        film = Films.objects.create(name=name, year=year, genre=genre, category=c, festival_name=f, producer=p)
    else:
        film = Films.objects.create(name=name, year=year, genre=genre, category=c, producer=p)

def create_recom(film, prod):
    f = Festival.objects.get(name=film)
    p = Producer.objects.get(name=prod)
    r = Recom.objects.create(name=f, author=p)


if __name__ == '__main__':

    Films.objects.filter(id=7).update(year=2010)

    # create_category('Выбор редакции')
    # create_producer('Эдгар Райт', 'Великобритания', 46)
    #
    # for i in ({'name': 'Скотт Пиллигрим против всех', 'year':'2010', 'genre':'Комедия', 'cat':'Комедия','fest': None, 'prod':'Эдгар Райт'},):
    #     create_films(i.get('name'), i.get('year'), i.get('genre'), i.get('cat'), i.get('fest'), i.get('prod'))

