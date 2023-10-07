from django.contrib import admin
from .models import ContactMessage
from .models import TeamMember


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email', 'subject')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio', 'photo')
    search_fields = ('name', 'role', 'bio')
