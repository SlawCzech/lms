from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'user'

urlpatterns = [
    path('registration/', views.registration_view, name="registration"),
    path('', lambda x: HttpResponse('thank you'), name='home')
]
