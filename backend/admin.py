from django.contrib import admin
from .models import Just
# Register your models here.


@admin.register(Just)
class Profile(admin.ModelAdmin):
    list_display = ['name']