from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from events.models import Event
from events.serializers import EventSerializer



@csrf_exempt
def index(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)
