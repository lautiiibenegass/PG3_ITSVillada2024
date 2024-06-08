from django.urls import path
from .views import get_rankings

urlpatterns = [
    path('', get_rankings, name='rankings'),
]
