from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email', 'subject')
