from django import forms
from .models import userData

class UserForm(forms.ModelForm):
    class Meta:
        model = userData
        fields = ['email', 'name', 'password']
