
from django.contrib import admin
from api.models import Contact


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'created_by',) ## for full data at admin page
