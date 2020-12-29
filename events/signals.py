from django.db.models.signals import post_save
from django.dispatch import receiver
from events.models import Event
from event_tickets.models import Ticket, TicketType


@receiver(post_save, sender=Event)
def create_tickets(sender, instance, created, **kwargs):
    if created:
        for ticket_type in TicketType.TICKET_TYPE:
            Ticket.objects.create(ticket_type=ticket_type[0], event=instance)
