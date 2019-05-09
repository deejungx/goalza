from django.db import models
from . import myFields

import datetime

# Default Opening and Closing Times for Futsal Companies

def getDefaultOpeningTime():
    return datetime.time(6,0)

def getDefaultClosingTime():
    return datetime.time(22,0)


class FutsalCompany(models.Model):

    futsal_id = models.AutoField(primary_key=True)
    futsal_name = models.CharField(max_length=155, unique=True)
    opening_time = models.TimeField(default=getDefaultOpeningTime)
    closing_time = models.TimeField(default=getDefaultClosingTime)

    class Meta:
        ordering = ['futsal_name']
        verbose_name_plural = 'futsal companies'

    def __str__(self):
        return self.futsal_name


class Ground(models.Model):

    ground_id = models.AutoField(primary_key=True)
    ground_number = models.IntegerField(unique=True)
    futsalCompany = models.ForeignKey(FutsalCompany, on_delete=models.CASCADE)
    ground_name = models.CharField(max_length=155, unique=True)
    # ground_status = models.BooleanField(default=False) # True for Occupied, False for Vacant

    def __str__(self):
        return self.ground_name

    class Meta:
        ordering = ['ground_number']



class Player(models.Model):

    player_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=12, unique=True)
    player_name = models.CharField(max_length=155)
    player_address = models.CharField(max_length=220, null=True, blank=True)
    player_email = models.EmailField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.player_name


class GroundPriceSegment(models.Model):

    price_segment_id = models.AutoField(primary_key=True)
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)
    day_of_week = myFields.DayOfTheWeekField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Booking(models.Model):


    # PAYMENT STATUS CHOICES
    PENDING = 'PENDING'
    COMPLETE = 'COMPLETE'
    # BOOKING STATUS CHOICES
    CONFIRMED = 'CONFIRMED'
    PLAYING = 'PLAYING'
    COMPLETE = 'COMPLETE'
    CANCELED = 'CANCELED'
    BOOKING_STATUS_CHOICES = (
        # (PENDING, 'PENDING CONFIRMATION'),
        (CONFIRMED, 'CONFIRMED'),
        (PLAYING, 'PLAYING'),
        (COMPLETE, 'COMPLETE'),
        (CANCELED, 'CANCELED'),
    )
    PAYMENT_STATUS_CHOICES = (
        (PENDING, 'PENDING'),
        (COMPLETE, 'COMPLETE'),
    )

    booking_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    booking_date = models.DateField()
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)
    start_time = models.TimeField()
    duration = models.DurationField()
    booking_status = models.CharField(
            max_length=50,
            choices=BOOKING_STATUS_CHOICES,
            default=CONFIRMED,
            )
    payment_status = models.CharField(
            max_length=50,
            choices=PAYMENT_STATUS_CHOICES,
            default=PENDING,
            )
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.booking_id
