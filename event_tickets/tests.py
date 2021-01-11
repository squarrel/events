from datetime import datetime
from django.test import Client, TestCase
from django.urls import reverse
from events.models import Event
from event_tickets.models import Ticket, TicketType, Reservation


class TestTicket(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ticket_create(self):
        date_time = datetime(2021, 1, 5, 20, 0, 0)
        date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
        event = Event.objects.create(name='AC/DC Concert', date_time=date_time)

        tickets_vip = Ticket.objects.get(event=event, ticket_type=TicketType.VIP)
        tickets_regular = Ticket.objects.get(event=event, ticket_type=TicketType.REGULAR)
        tickets_premium = Ticket.objects.get(event=event, ticket_type=TicketType.PREMIUM)

        tickets = Ticket.objects.all()
        self.assertEqual(len(tickets), 3)

    def test_reservation(self):
        date_time = datetime(2021, 1, 5, 20, 0, 0)
        date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
        event = Event.objects.create(name='AC/DC Concert', date_time=date_time)

        tickets_vip = Ticket.objects.get(event=event, ticket_type=TicketType.VIP)
        tickets_regular = Ticket.objects.get(event=event, ticket_type=TicketType.REGULAR)
        tickets_premium = Ticket.objects.get(event=event, ticket_type=TicketType.PREMIUM)
        tickets_vip.quantity = 300
        tickets_regular.quantity = 300
        tickets_premium.quantity = 300
        tickets_vip.save()
        tickets_regular.save()
        tickets_premium.save()

        response = self.client.get(
            reverse(
                'reserve',
                kwargs = {
                    'event_id': event.id, 'ticket_type': TicketType.REGULAR,
                    'first_name': 'Pera', 'last_name': 'Petrovic'
                }
            )
        )

        self.assertEqual(200, response.status_code)

        reservations = Reservation.objects.filter(event=event, ticket_type=TicketType.REGULAR)
        self.assertEqual(len(reservations), 1)
