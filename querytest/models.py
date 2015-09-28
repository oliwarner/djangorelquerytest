from django.db import models


class Category(models.Model):
    pass


class Agent(models.Model):
    categories = models.ManyToManyField('Category')


class Booking(models.Model):
    agent = models.ForeignKey('Agent')
    category = models.ForeignKey('Category')
