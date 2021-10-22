from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import bloggers, zayavki

# Register your models here.
class bloggersAdmin(ModelAdmin):
    list_display = ["name", "platform", "profile_link", "followersnumber", "phone"]
    list_filter = ["platform", "followersnumber"]


class zayavkiAdmin(ModelAdmin):
    list_display = ["name", "phone_number", "text", "date_created"]
    list_filter = ["date_created"]


admin.site.register(bloggers, bloggersAdmin)
admin.site.register(zayavki, zayavkiAdmin)
