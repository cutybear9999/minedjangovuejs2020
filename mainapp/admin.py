from django.contrib import admin
from mainapp.models import Note
from mainapp.models import DBItem

# Register your models here.
admin.site.register(Note)
admin.site.register(DBItem)
