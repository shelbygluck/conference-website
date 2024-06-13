from typing import Any
from django.shortcuts import render

from .models import ConferenceUser
# import generic views
from django.views.generic import CreateView

# import login view
from django.contrib.auth.views import LoginView

from .forms import ConferenceUserForm, LoginForm
from django.contrib.auth import authenticate, login

# import messages
from django.contrib import messages

# Create your views here.

# Create registration view
class RegisterView(CreateView):
    model = ConferenceUser
    form_class = ConferenceUserForm
    template_name = 'generic_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        context['header'] = 'Sign up for an account'
        context['button_text'] = 'Register'
        return context

    def form_valid(self, form):
        # Save the user first, then add the user to the group
        # create the user
        user = form.save()
        # set the password
        user.set_password(form.cleaned_data.get('password'))
        # save the user
        user.save()
        return super().form_valid(form)

# Create login view
class LoginUserView(LoginView):
    template_name = 'generic_form.html'
    success_url = '/'
    form_class = LoginForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['header'] = 'Login to your account'
        context['button_text'] = 'Login'
        return context
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self) -> str:
        # Get next from querystring
        # If no value, return to /
        next_url = self.request.GET.get('next', '/')
        return next_url