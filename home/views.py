from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

from home.forms import SignInForm, SignUpForm

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class LoginInterfaceView(LoginView):
    form_class = SignInForm
    template_name='home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'home/signup.html'
    success_url = reverse_lazy('login')