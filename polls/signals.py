# from django.contrib.auth.models import User
# from .models import *
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#   if created:
#     User.objects.create(username=instance)
#
#
# post_save.connect(create_user_profile, sender=User)
#
#
# @receiver(post_save, sender=Store)
# def save_user_profile(sender, instance, created, **kwargs):
#   instance.store.save()
#
#
# post_save.connect(create_user_profile, sender=Store)
