from django.db import models
from django.utils.translation import gettext_lazy as _


class TrainClass(models.Model):
    className = models.CharField(_("Seat Class"), max_length=255)
    SeatQuota = models.CharField(_("Seat Quota"), max_length=255)
    totalSeats = models.IntegerField(_("Total Seats"), default=0)
    availSeats = models.IntegerField(_("Avaiable Seats"), default=0)

    def __str__(self):
        return str(self.className) + " " + str(self.SeatQuota)

class Train(models.Model):
    trainName = models.CharField(_("Train Name"), max_length=255)
    trainNumber = models.CharField(_("Train Number"), primary_key=True, max_length=6)
    coach = models.ManyToManyField(TrainClass)

    def __str__(self):
        return self.trainName


class Seat(models.Model):
    train = models.ForeignKey(Train)
    coach = models.ForeignKey(TrainClass)
    name = models.CharField(_("Seat No."),max_length=5)
    available = models.BooleanField(_("Booked"),default=False)
    seatType = models.CharField(_("Berth Type"), max_length=2)

    def __str__(self):
        return self.name