# Django model relationships

---

## 1. [One to One](https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/)

One row of table A linked with one row of table B, (normal :) - hus-wife analogy)\
Eg:-
| ID  | Username | passw  |
| --- | -------- | ------ |
| 1   | Akshay   | Aks123 |

There is a page model, one user can make only one page.

| ID  | page_no | page_info | date       |
| --- | ------- | --------- | ---------- |
| 1   | ww      | news      | 11-09-2003 |

In django, one to one relation is defined using OnetoOne field,

syntax:- `OneToOneField(to, on_delete, parent_link-False, **options)`

Attributes

* `to`  --> To which model the relation is to be specified.
* `on_delete` --> Behavior when deleted, (eg: CASCADE..)
  When an object referenced by a foreign key is deleted, django will emulate the behavior of the SQL constraint specified by `on_delete`.
  Eg:- \
  * CASCADE:- emulates the behavior of SQL constraint ON DELETE CASCADE, also delete the ForeignKey related object too, ie if a user is deleted the pages created by him also deleted.
  * PROTECT:- Prevents deletion of the related object by raising a ProtectedError(sub class of django.db.IntegrityError)
  * SET_NULL:- ForeignKey to null, (only if null=True)
  * SET_DEFAULT:- Set FK, the default value set( a default must be set)
  * SET():- Explicitly set the FK value to the passed value to SET(), if a fn./callable passed the result of it.
  * DO_NOTHING:- Cause an IntegrityError.

* `parent_link=True` (False is the default value): - If the model is inherited from another model, ie
  A and B(A), there will be one-to-one relation set b/w them automatically, for parent_link=True.. That relation is used rather than the explicit one created with the field.
* `limit_choices_to` --> set who can create relations, (ie pages according to our example), if only staffs are allowed to create pages etc that can be set using limit_choices_to option.
* `related_name`:- Which is simply the name of the relation, that is used by the related object(here pages) to connect with this(parent) one. In some cases there not needed a backward relation, set related name to '+' or end it with '+'.

There are some other options, lets use them in an example to get mores sense.

* Creating a sample project (akshay.dev, testproject)

* Disble the newly added sidebar in django, i sometimes looks weird on the top because the old css is preloaded in the browser do a (ctrl + F5), clear the cache and the sidebar gets normal.

  ```python
  from django.contrib import admin

  admin.autodiscover()
  admin.site.enable_nav_sidebar = False
  ```

* Create a model that got a one-to-one relation to the User model.

  ```python
  from django.db import models
  from django.contrib.auth.models import User

  class Page(models.Model):
      # name given as to identify which model it is related.
      user = models.OneToOneField(
          User, on_delete=models.CASCADE, primary_key=True)
      page_name = models.CharField(max_length=100)
      page_info = models.CharField(max_length=200)
      date = models.DateField()
  ```

* Register the models in admin page.

  ```python
  from django.contrib import admin
  from basics.models import Page

  # admin.site.register(Page)

  @admin.register(Page)
  class PageAdmin(admin.ModelAdmin):
      list_display = ['page_name', 'page_info', 'date', 'user']

  ```

* Add some dummy users.
* Because the user field is attached to the pages with one to one relation, we can see all the users listed in the dropdown.
* If tried to add a page with the same user for the second time, it fails and say, "`Page with this User already exists.`" Thats what the one-to-one relation means.
* If we look at the created table (in sqlite), the primary key is set to user_id(ie the pk of user, we set this at creation, `primary_key=True`)
* If you delete a user, his created page gone too.
* This can be implemented in practical cases like profiles of a user, if user deletes the page, his profile gone too
* If needed to protect the profile, use `on_delete=models.PROTECT`, now if tried to delete the user, a warning occurs saying the page is protected.
* Limit who can set the pages:-

  ```python
  user = models.OneToOneField(
          User, on_delete=models.CASCADE, primary_key=True,
          limit_choices_to={'is_staff': True})
  ```

## Customizing the relation using signals

* If we need a custom relation for eg, If the page gets deleted, we need the user also to be gone( like CASCADE relation in both direction).
* For that kind of extra logic make a separate script file (signals.py), write the logic there register it in the app.
* Eg:- Sample logic,

  ```python
  from .models import Page
  from django.db.models.signals import post_delete
  # to connect the signal use a receiver
  from django.dispatch import receiver

  # receiver is something that can be related with the event-listeners in JS


  @receiver(post_delete, sender=Page)
  def delete_related_user(sender, instance, **kwargs):
      """Delete the created user too when deleting a profile page

      Args:
          sender ([type]): [description]
          instance ([type]): [description]
      """
      print("Page Post_Delete")

      instance.user.delete()

  # Finds which user is deleting the page and post request is captured by the receiver, that user is then deleted

  ```

* Resister it in `apps.py`.

  ```python
  from django.apps import AppConfig


  class BasicsConfig(AppConfig):
      name = 'basics'

      def ready(self):
          import basics.signals
  ```

* Also add the config in `__init__` of the app, `default_app_config = 'basics.apps.BasicsConfig'`
* Checking it, create a page with a dummy user, delete the page now the user is deleted too, got the message `Page Post_Delete`.

## Model inheritance

* Lets create an inherited model, Like inherited from Page, and explicitly add a one-to-one relation to it.

  ```python
  class Like(Page):
      """
      Inherited field also got the OneToOne relationship with the parent,
      added an extra one-to-one to look up the scenario
      """
      page_in = models.OneToOneField(
          User, on_delete=models.CASCADE, primary_key=True, parent_link=True)
      likes = models.IntegerField()

  ```

* register it too in the admin area,

  ```python
  @admin.register(Like)
  class LikeAdmin(admin.ModelAdmin):
      list_display = ['page_in', 'page_name',
                      'page_info', 'date', 'user', 'likes']
  ```

* Now a one-to-one relation is added explicitly, looking at the sql table a new key, ('page_in_id') replaces the inherited id ('page_ptr_id). cz the primary key is set true in the relation.
* Now a like object is created by a user, a page object is created automatically.
