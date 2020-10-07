from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class HelloWold(View):
    def get(self, request):
        html = f"""<h1>Hello World!</h1>"""
        return HttpResponse(html)

# Create your views here.
