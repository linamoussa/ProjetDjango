from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Participant, Reservation

#admin.TabularInline see difference
class ReservationInline(admin.StackedInline):
    model = Reservation
    extra = 1
    readonly_fields = ('reservation_date',)
    can_delete = True

def confirm_reservations(modeladmin, request, queryset):
    for reservation in queryset:
        reservation.confirmed = True
        reservation.save()

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'participant_category', 'created_at', 'total_reservations')
    
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    list_filter = ('participant_category', 'created_at')
    
    def total_reservations(self, obj):
        return Reservation.objects.filter(participant=obj).count()
    
    total_reservations.short_description = 'Total Reservations'
    inlines = [ReservationInline]

class ReservationAdmin(admin.ModelAdmin):
    list_display=('reservation_date','conference','participant','confirmed')
    actions=['confirmed','unconfirmed']
    def confirmed(self,request,queryset):
        queryset.update(confirmed=True)
        self.message_user(request,"Les reservations sont confirmées")  
    confirmed.short_descriptions="Reservations à confirmer"  
    def unconfirmed(self,request,queryset):
        queryset.update(confirmed=False)
        self.message_user(request,"Les reservations sont non confirmées")
    unconfirmed.short_descriptions="Reservations à non confirmer"  

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Reservation, ReservationAdmin)
