from django.urls import path
from playground import views

urlpatterns = [
    path('hello/', views.say_hello, name='hello '),
    path('send_mail/', views.send_mail_message, name="send_email_message"),
]
