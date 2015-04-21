from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Route(models.Model):
    date = models.DateField(_("Date of journey"), default=datetime.date(datetime.now()))
