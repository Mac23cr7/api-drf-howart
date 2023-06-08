from django.urls import path
from apps.home.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]

