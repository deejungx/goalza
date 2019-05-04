from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from pages.models import FutsalCompany


class CustomUser(AbstractUser):
    is_futsal_admin = models.BooleanField(default=True)  # Futsal admin's is_staff property should be set to False in production

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True,
                                on_delete=models.CASCADE)
    futsal = models.ForeignKey(FutsalCompany, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
