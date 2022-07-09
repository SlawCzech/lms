from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms

def home_view(request):
    return HttpResponse('elo')

def registration_view(request):
    if request.method =='POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect(reverse_lazy('user:home'))
    else:
        form = forms.RegistrationForm()
    return render(request, 'user/registration.html', {'form':form})
