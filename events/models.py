from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=233)
    date_time = models.DateTimeField(null=False)
