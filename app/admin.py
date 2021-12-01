from django.contrib import admin

from .models import Calendar
from .models import troupes

admin.site.register(Calendar)
admin.site.register(troupes)
