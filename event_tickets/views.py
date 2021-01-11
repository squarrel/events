import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from event_tickets.models import Ticket, Reservation, TicketType
from event_tickets.serializers import ReservationSerializer, TicketSerializer


@csrf_exempt
def index(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return JsonResponse(serializer.data, safe=False)


def available(request, event_id):
    tickets = Ticket.objects.filter(event_id=event_id)
    result = dict()
    for ticket in tickets:
        result[ticket.ticket_type] = ticket.available()

    return JsonResponse(result)


def reserve(request, event_id, ticket_type, first_name, last_name):
    reservation = Reservation.objects.create(
        event_id=event_id, ticket_type=ticket_type,
        first_name=first_name, last_name=last_name
    )

    serializer = ReservationSerializer(reservation)
    return JsonResponse(serializer.data, safe=False)


def buy(request, event_id, ticket_type):
    tickets = Ticket.objects.get(event_id=event_id, ticket_type=ticket_type)
    reservation = None

    try:
        reservation = Reservation.objects.get(event_id=event_id, ticket_type=ticket_type, active=True)
    except Reservation.DoesNotExist:
        pass

    if (reservation and reservation.valid) or tickets.available > 0:
        if reservation:
            reservation.active = False
            reservation.save()

        tickets.reduce_quantity(1)
        tickets.save()
