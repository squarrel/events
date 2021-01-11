import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from event_tickets.models import Ticket, Reservation
from event_tickets.serializers import TicketSerializer


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
