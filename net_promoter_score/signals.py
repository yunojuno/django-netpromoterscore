from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from .models import UserScore

# custom signal sent when a new score is submitted
new_nps_score = Signal(providing_args=["instance"])


@receiver(post_save, sender=UserScore)
def on_new_score(sender, instance, created, **kwargs):
    # this is a pass-through that filters just new objects
    if not created:
        return
    new_nps_score.send(sender=sender, instance=instance)
