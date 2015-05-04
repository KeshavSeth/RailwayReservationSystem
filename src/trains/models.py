from django.db import models
from django.utils.translation import gettext_lazy as _


class Bogey(models.Model):
    className = models.CharField(_("Seat Class"), max_length=255)
    seatQuota = models.CharField(_("Seat Quota"), max_length=255)
    fare = models.PositiveIntegerField(_("Fare"), default=0)

    def __str__(self):
        return str(self.className) + " " + str(self.seatQuota)


class TrainClass(models.Model):
    bogey = models.ForeignKey(Bogey)
    totalSeats = models.IntegerField(_("Total Seats"), default=0)
    availSeats = models.IntegerField(_("Avaiable Seats"), default=0)

    def __str__(self):
        return str(self.bogey) + " | " + str(self.availSeats) + " left"


class TrainManager(models.Manager):

    def get_train(self, train_id):
        return Train.objects.values().get(trainNumber=train_id)['trainName']


class Train(models.Model):
    trainName = models.CharField(_("Train Name"), max_length=255)
    trainNumber = models.CharField(
        _("Train Number"), primary_key=True, max_length=6)
    coach = models.ManyToManyField(TrainClass)
    objects = TrainManager()

    def __str__(self):
        return self.trainName


class Seat(models.Model):
    LOWER = 'LO'
    MIDDLE = 'MI'
    UPPER = 'UP'

    BERTH_TYPE = (
        (LOWER, 'lower'),
        (MIDDLE, 'middle'),
        (UPPER, 'upper'),
    )

    train = models.ForeignKey(Train)
    coach = models.ForeignKey(TrainClass)
    name = models.CharField(_("Seat No."), max_length=5)
    available = models.BooleanField(_("Booked"), default=False)
    seatType = models.CharField(
        _("Berth Type"), max_length=2, choices=BERTH_TYPE, default='lower')

    def quota(self):
        return self.coach.seatQuota

    def __str__(self):
        return self.name
