from django.contrib import admin

# Register your models here.
from .models import Choice, Vote, Polllist

admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(Polllist)

