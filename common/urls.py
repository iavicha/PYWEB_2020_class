from django.urls import path
from .views import DataTimeView
from .views import RandomNumber
from .views import IndexView

urlpatterns = [
    path('datetime/', DataTimeView.as_view()),
    path('random/', RandomNumber.as_view()),
    path('', IndexView.as_view())
]
