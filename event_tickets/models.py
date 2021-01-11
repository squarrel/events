from datetime import timedelta

from django.db import models
from django.utils import timezone
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

    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    ticket_type = models.IntegerField(choices=TicketType.TICKET_TYPE, default=0)
    quantity = models.IntegerField(default=0)

    def reduce_quantity(self, amount):
        self.quantity -= amount

    def available(self):
        reserved = Reservation.objects.filter(event=self.event, ticket_type=self.ticket_type, active=True)
        result = self.quantity
        for r in reserved:
            if r.valid:
                result -= 1
        return result

    class Meta:
        unique_together = ('event', 'ticket_type')


class Reservation(models.Model):

    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    ticket_type = models.IntegerField(choices=TicketType.TICKET_TYPE, null=False)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=15)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    active = models.BooleanField(default=True)

    @property
    def valid(self):
        now = timezone.now()
        discrepancy = now-self.start_time
        disc_minutes = discrepancy.total_seconds() / 60
        if disc_minutes < self.duration:
            return True
        return False
