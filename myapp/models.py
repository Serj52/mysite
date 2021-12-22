from django.db import models


class Author (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
    def __str__(self):
        return self.name

# Create your models here.
##############################################################################################

class Producer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Festival(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Films(models.Model):
    name = models.CharField(max_length=255, unique=True)
    year = models.IntegerField(max_length=3000)
    festival_name = models.ForeignKey(Festival, null=True)
    category = models.ForeignKey(Category)
    genre = models.CharField(max_length=255)
    producer = models.ForeignKey(Producer)
    def __str__(self):
        return self.name

class Recom(models.Model):
    name = models.ForeignKey(Films)
    author = models.ForeignKey(Producer)
    def __str__(self):
        return self.name

















