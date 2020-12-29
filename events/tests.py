from datetime import datetime
from django.test import TestCase
from events.models import Event


class TestEvent(TestCase):

    def test_event_create(self):
        date_time = datetime(2021, 1, 5, 20, 0, 0)
        date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
        event = Event.objects.create(name='AC/DC Concert', date_time=date_time)

        events = Event.objects.all()
        self.assertEqual(len(events), 1)
