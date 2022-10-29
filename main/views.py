from django.views.generic import TemplateView, FormView
from .forms import LoginForm, RegisterForm

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class LoginView(FormView):
    template_name = 'main/login.html'
    form_class = LoginForm
    success_url = '/thank-you'

class RegisterView(FormView):
    template_name = 'main/registration.html'
    form_class = RegisterForm
    success_url = '/'
