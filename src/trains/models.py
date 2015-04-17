from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Train(models.Model):
    trainName = models.CharField(_("Train Name"), max_length=255)
    trainNumber = models.CharField(
        _("Train Number"), primary_key=True, max_length=6)

    def __str__(self):
        return self.trainName


class TrainClass(models.Model):
    train = models.ForeignKey(Train, default=0)
    className = models.CharField(_("Seat Class"), max_length=255)
    SeatQuota = models.CharField(_("Seat Quota"), max_length=255)
    totalSeats = models.IntegerField(_("Total Seats"), default=0)
    availSeats = models.IntegerField(_("Avaiable Seats"), default=0)

    def __str__(self):
        return self.className
