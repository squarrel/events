from django.db import models
from event_tickets.models import Ticket, Reservation, TicketType


class Event(models.Model):

    name = models.CharField(max_length=233)
    date_time = models.DateTimeField(null=False)
