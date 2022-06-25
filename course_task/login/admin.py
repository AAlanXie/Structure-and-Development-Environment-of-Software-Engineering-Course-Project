from django.contrib import admin

# Register your models here.

from .models import Information,Event

admin.site.register(Information)
admin.site.register(Event)
