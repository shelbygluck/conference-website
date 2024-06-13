from django.contrib import admin

# Register your models here.
from .models import Talk, Track

admin.site.register(Talk)
admin.site.register(Track)
