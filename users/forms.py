from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import views

class UserCreationForm():
    form = UserCreationForm
    class Meta:
        fields = ('username', 'password1', 'password2')
        model = User
        