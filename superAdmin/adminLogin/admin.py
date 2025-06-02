from django.contrib import admin

from .models import myUsers

# Register your models here.
class myUsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']

admin.site.register(myUsers, myUsersAdmin)