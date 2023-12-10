from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login


# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'auth/login.html'
    next_page = reverse_lazy('todo:main')

    def form_valid(self, form):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, form.get_user())
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(reverse_lazy('login')+'?active=false')

class UserLogoutView(LogoutView):
    next_page = 'login'