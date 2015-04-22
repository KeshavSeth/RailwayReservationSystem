from django.contrib import admin
from trains.models import *

def unbound_callable(seat):
    return seat.train.trainName


class SeatInline(admin.TabularInline):
	model = Seat
	fields = ('name', 'model_callable', 'model_admin_callable', unbound_callable)
	readonly_fields = ('model_callable', 'model_admin_callable', unbound_callable)

	def model_admin_callable(self, seat):
		return seat.train.trainName

class TrainClassAdmin(admin.ModelAdmin):
	model = TrainClass
	inlines = (SeatInline,)

admin.site.register(Train)
admin.site.register(TrainClass, TrainClassAdmin)
admin.site.register(Seat)