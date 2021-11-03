from django.shortcuts import render
from django.views.generic import View
from .models import Calendar


class IndexView(View):
    def get(self, request, *args, **kwargs):
        calendar_data = Calendar.objects.all()
        if calendar_data.exists():
            calendar_data = calendar_data.order_by('-id')[0]
        return render(request, 'app/index.html', {
            'calendar_data' : calendar_data
        })
"""

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myapp/index.html')

"""