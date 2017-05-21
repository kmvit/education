from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class PersonInline(admin.TabularInline):
    model = Person

class UserAdmin(admin.ModelAdmin):
    inlines = [
        PersonInline,
    ]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Country)
admin.site.register(Person)