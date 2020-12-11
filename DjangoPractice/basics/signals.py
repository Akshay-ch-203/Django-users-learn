from .models import Page
from django.db.models.signals import post_delete
# to connect the signal use a receiver
from django.dispatch import receiver

# Signals is something that can be related with the event-listeners in JS


@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    """Delete the created user too when deleting a profile page

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
    """
    print("Page Post_Delete")

    instance.user.delete()

# Finds which user is deleting the page and post request is captured by the
# receiver, that user is then deleted
