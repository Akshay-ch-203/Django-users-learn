from django.db import models
from django.contrib.auth.models import User

# use the default user model ()
# class User(models.Model):
#     user_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)


class Page(models.Model):
    # name given as to identify which model it is related.
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, primary_key=True,
    #     limit_choices_to={'is_staff': True})
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=100)
    page_info = models.CharField(max_length=200)
    date = models.DateField()


class Like(Page):
    """
    Inherited field also got the OneToOne relationship with the parent
    """
    page_in = models.OneToOneField(
        Page, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()
