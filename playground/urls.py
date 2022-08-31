from django.urls import path
from . import views

#URL config / routes
urlpatterns = [
    path('hello/',views.say_hello)
]