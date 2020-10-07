from django.urls import path
from .views import HelloWold

urlpatterns = [
    path('hello/', HelloWold.as_view())
]