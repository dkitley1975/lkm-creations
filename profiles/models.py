from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    # registration details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User: address details
    default_street_address1 = models.CharField(
        max_length=80,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("User Address Line 1"),
        help_text=("format: max_length: 80"),
    )
    default_street_address2 = models.CharField(
        max_length=80,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("User Address Line 2"),
        help_text=("format: max_length: 80"),
    )
    default_town_or_city = models.CharField(
        max_length=50,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("User Town or City"),
        help_text=("format: max_length: 50"),
    )
    default_county = models.CharField(
        max_length=50,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("User County"),
        help_text=("format: max_length: 50"),
    )
    default_country = CountryField(
        unique=False,
        blank=True,
        null=True,
        blank_label="Select Country",
    )
    default_postcode = models.CharField(
        max_length=10,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("User Postcode"),
        help_text=("format: max_length: 10"),
    )

    # user contact details
    default_phone_number = models.CharField(
        max_length=20,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("User Main Contact Number"),
        help_text=("format: max_length: 20"),
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    When a user is created, create a UserProfile for that user.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
