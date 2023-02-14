from django.contrib import admin
from .models import BernLog, MarlyLog

# Register your models here.

class BernLogAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "action", "comments", "initials")

class MarlyLogAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "action", "comments", "initials")

# Register model

admin.site.register(BernLog, BernLogAdmin)
admin.site.register(MarlyLog, MarlyLogAdmin)



