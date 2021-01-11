from django.contrib import admin
from event_tickets.models import Reservation, Ticket


class TicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ticket, TicketAdmin)


class ReservationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reservation, ReservationAdmin)
