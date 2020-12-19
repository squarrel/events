from django.db import models
from events.models import Event


class TicketType:

    REGULAR = 0
    PREMIUM = 1
    VIP = 2

    TICKET_TYPE = (
        (REGULAR, 'Regular'),
        (PREMIUM, 'Premium'),
        (VIP, 'VIP'),
    )


class Ticket(models.Model):

    event = models.ForeignKey(Event, null=False)
    ticket_type = models.IntegerField(choices=TicketType.TICKET_TYPE, default=0)
    available = models.IntegerField(default=0)

    def reduce(self, amount):
        self.available -= amount

    class Meta:
        unique_together = ('event', 'ticket_type')


class Reservation(models.Model):

    event = models.ForeignKey(Event, null=False)
    ticket_type = models.IntegerField(choices=TicketType.TICKET_TYPE, null=False)
    start_time = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(default=15)
    valid = models.BooleanField(default=False)
