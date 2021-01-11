from datetime import datetime
from django.test import TestCase
from events.models import Event
from event_tickets.models import Ticket, TicketType, Reservation


class TestTicket(TestCase):

    def test_ticket_create(self):
        date_time = datetime(2021, 1, 5, 20, 0, 0)
        date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
        event = Event.objects.create(name='AC/DC Concert', date_time=date_time)

        tickets_vip = Ticket.objects.get(event=event, ticket_type=TicketType.VIP)
        tickets_regular = Ticket.objects.get(event=event, ticket_type=TicketType.REGULAR)
        tickets_premium = Ticket.objects.get(event=event, ticket_type=TicketType.PREMIUM)

        tickets = Ticket.objects.all()
        self.assertEqual(len(tickets), 3)
