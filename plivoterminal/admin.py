from django.contrib import admin
from .models import Incoming

class IncomingAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'date_time','contents',)
    search_fields = ('phone_number', 'date_time','contents',)

admin.site.register(Incoming, IncomingAdmin)
