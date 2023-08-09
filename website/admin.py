from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "zipcode", "created_at")
