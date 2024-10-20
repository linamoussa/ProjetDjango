from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Conference
from users.models import *
from django.db.models import Count
# Register your models here.
class ReservationInline(admin.StackedInline):
    model=Reservation
    extra=1
    readonly_fields=('reservation_date',)
    can_delete=True
class ParticipantFilter(admin.SimpleListFilter):
    title="participant filter"
    parameter_name="participant"
    # Pour l'affichage
    def lookups(self, request: Any, model_admin: Any):
        return (
            ('0',('No participants')),
            ('more',('More participants'))
        )
    """
    def queryset(self, request: Any, queryset: QuerySet[Any]):
        if self.value()=='0':
            # calculer les reservations dans une conférence + filtrer 
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count=0)
        if self.value()=='more':
            #gt : greater then
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count__gt=0)        
        return queryset
    """
    def queryset(self, request: Any, queryset: QuerySet[Any]):
        if self.value()=='0':
            return queryset.filter(reservations__isnull=True)
        if self.value()=='more':
            return queryset.filter(reservations__isnull=False)       
        return queryset
    
class ConferenceDateFilter(admin.SimpleListFilter):
    title="date conf filter"
    parameter_name="conference_date"
    def lookups(self, request: Any, model_admin: Any):
        return (
            ('past',('Past conferences')),
            ('upcoming',('Upcoming conferences')),
            ('today',('Today conferences'))
        )
    def queryset(self, request: Any, queryset: QuerySet[Any]):
        if self.value()=='past':
            return queryset.filter(end_date__lt=timezone.now().date()) 
        if self.value()=='today':
            return queryset.filter(start_date=timezone.now().date()) 
        if self.value()=='upcoming':
            return queryset.filter(start_date__gt=timezone.now().date()) 
        return queryset
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title','location','start_date','end_date','price')
    search_fields = ('title',)
    list_per_page=2
    #Reverse ordering ('-start_date','title')
    ordering=('start_date','title')
    fieldsets=(
        ('Description', {
            'fields':('title','description','category','location')
        }),
        ('Horaire',{
            'fields':('start_date','end_date')
        }),
        ('Documents',{
            'fields':('program',)
        })
    )
    readonly_fields=('created_at','updated_at')
    inlines=[ReservationInline]
    autocomplete_fields=('category',)
    list_filter=('title',ParticipantFilter,ConferenceDateFilter)
admin.site.register(Conference,ConferenceAdmin)