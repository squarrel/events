from rest_framework import serializers
from event_tickets.models import Ticket, Reservation


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['event', 'ticket_type', 'quantity']


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['event', 'ticket_type', 'first_name', 'last_name', 'start_time']
