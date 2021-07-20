from django.contrib import admin
from .models import *

class NewsletterAdmin(admin.ModelAdmin):
    list_display  = ('email', 'date_added',)




def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(NewletterUser)
admin.site.register(Newsletter, NewsletterAdmin)