from django.contrib import admin
from profileapp.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    exclude = ()

admin.site.register(Profile, ProfileAdmin)