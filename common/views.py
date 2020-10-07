from datetime import datetime
import random
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class DataTimeView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)


class RandomNumber(View):
    def get(self, request):
        html = f'{random.randint(0, 1000)}'
        return HttpResponse(html)

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')

# Create your views here.
