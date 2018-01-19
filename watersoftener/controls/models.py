from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from helper.day_of_week import DayOfTheWeekField

# Create your models here.

class ControlsModel(models.Model):
    salt_level = models.FloatField(
        validators= [MinValueValidator(0.0), MaxValueValidator(1.0)]
    )
    vacation_mode = models.BooleanField(default=False)
    days_away = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    system_alarm = models.BooleanField(default=False)
    system_alarm_time = models.TimeField()
    time_of_day = models.TimeField()
    current_day_of_week = DayOfTheWeekField()
    current_date = models.DateField()
    auto_dst = models.BooleanField(default=True)
