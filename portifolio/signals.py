from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import *

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )
        print("Profile created")

def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.Profile.first_name = instance.first_name
        instance.Profile.last_name = instance.last_name
        instance.Profile.email = instance.email
        instance.Profile.save()

        print("Profile updated successfully")

post_save.connect(create_profile, sender=User)
pre_save.connect(update_profile, sender=User)
