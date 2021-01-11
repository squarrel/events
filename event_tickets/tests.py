from datetime import datetime
from django.test import Client, TestCase
from django.urls import reverse
from events.models import Event
from event_tickets.models import Ticket, TicketType, Reservation


class TestTicket(TestCase):
    def setUp(self):
        self.client = Client()

        date_time = datetime(2021, 1, 5, 20, 0, 0)
        date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
        self.event = Event.objects.create(name='AC/DC Concert', date_time=date_time)

        self.tickets_vip = Ticket.objects.get(event=self.event, ticket_type=TicketType.VIP)
        self.tickets_regular = Ticket.objects.get(event=self.event, ticket_type=TicketType.REGULAR)
        self.tickets_premium = Ticket.objects.get(event=self.event, ticket_type=TicketType.PREMIUM)

    def test_ticket_create(self):
        tickets = Ticket.objects.all()
        self.assertEqual(len(tickets), 3)

    def test_reservation(self):
        self.tickets_vip.quantity = 300
        self.tickets_regular.quantity = 300
        self.tickets_premium.quantity = 300
        self.tickets_vip.save()
        self.tickets_regular.save()
        self.tickets_premium.save()

        response = self.client.get(
            reverse(
                'reserve',
                kwargs = {
                    'event_id': self.event.id, 'ticket_type': TicketType.REGULAR,
                    'first_name': 'Pera', 'last_name': 'Petrovic'
                }
            )
        )

        self.assertEqual(200, response.status_code)

        reservations = Reservation.objects.filter(event=self.event, ticket_type=TicketType.REGULAR)
        self.assertEqual(len(reservations), 1)

    def test_buy_without_reservation(self):
        self.tickets_vip.quantity = 300
        self.tickets_regular.quantity = 300
        self.tickets_premium.quantity = 300
        self.tickets_vip.save()
        self.tickets_regular.save()
        self.tickets_premium.save()

        response = self.client.get(
            reverse(
                'buy',
                kwargs = {
                    'event_id': self.event.id, 'ticket_type': TicketType.PREMIUM
                }
            )
        )

        self.assertEqual(200, response.status_code)

        tickets_premium = Ticket.objects.get(event=self.event, ticket_type=TicketType.PREMIUM)
        self.assertEqual(299, tickets_premium.quantity)
