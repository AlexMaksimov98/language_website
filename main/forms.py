from django.forms import ModelForm
from .models import User, NewUser

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RegisterForm(ModelForm):
    class Meta:
        model = NewUser
        fields = '__all__'