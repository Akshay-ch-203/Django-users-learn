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
