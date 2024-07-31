from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse
from .models import *


# decorator
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('User profile created successfully')
    else:
        print('Error occured, Profile not created.')



@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    
    try:
        if created == False:
            instance.Profile.save()
            print('Profile updated successfully')
    except:
        instance.profile = None