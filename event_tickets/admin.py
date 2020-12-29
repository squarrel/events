from django.contrib import admin
from event_tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ticket, TicketAdmin)
