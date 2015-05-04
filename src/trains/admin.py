from django.contrib import admin
from trains.models import *


def unbound_callable(seat):
    return seat.coach.seatQuota


class SeatInline(admin.TabularInline):
    model = Seat
    fields = ('name', 'quota', unbound_callable)
    readonly_fields = ('quota', unbound_callable)

    def model_admin_callable(self, seat):
        return seat.train.trainName


class TrainClassAdmin(admin.ModelAdmin):
    model = TrainClass
    inlines = (SeatInline,)

admin.site.register(Train)
admin.site.register(Bogey)
admin.site.register(TrainClass)
admin.site.register(Seat)
