from django.contrib import admin
from account.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','avatar','location',)
    list_filter = ('user','location',)
    search_fields = ('user',)


admin.site.register(Profile, ProfileAdmin)