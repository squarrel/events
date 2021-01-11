from rest_framework import serializers
from event_tickets.models import Ticket, Reservation


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['event', 'ticket_type', 'quantity']
