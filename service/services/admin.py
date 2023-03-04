from django.contrib import admin

from services.models import Service, Plan, Subcription

admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subcription)
