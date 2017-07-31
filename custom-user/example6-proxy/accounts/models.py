from django.db import models
from django.contrib.auth.models import User


class PersonManager(models.Manager):
    pass


class Person(User):
    objects = PersonManager()

    class Meta:
        ordering = ['last_name']
        proxy = True

    def do_something(self):
        pass
