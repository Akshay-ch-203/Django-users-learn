from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class Page(models.Model):
    # name given to quickly get to which model it is related.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=100)
    page_info = models.CharField(max_length=200)
    date = models.DateField()
