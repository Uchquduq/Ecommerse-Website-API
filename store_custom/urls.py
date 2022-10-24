from django.urls import path
from store_custom import views

urlpatterns = [
    path("", views.say_hello, name="hello"),
    
]