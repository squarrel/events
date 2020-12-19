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

    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    ticket_type = models.IntegerField(choices=TicketType.TICKET_TYPE, default=0)
    quantity = models.IntegerField(default=0)

    def reduce_quantity(self, amount):
        self.quantity -= amount

    def available(self, event, ticket_type):
        reserved = Reservation.objects.filter(valid=True, event=event, ticket_type=ticket_type)
        result = self.available - reserved
        return result

    class Meta:
        unique_together = ('event', 'ticket_type')


class Reservation(models.Model):

    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    ticket_type = models.IntegerField(choices=TicketType.TICKET_TYPE, null=False)
    start_time = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(default=15)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    @property
    def valid(self):
        now = timezone.now()
        discrepancy = timedelta(now-start_time)
        if discrepancy < self.duration:
            return True
        return False
