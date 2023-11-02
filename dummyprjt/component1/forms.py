from django import forms
from .models import userData #must import forms and the model you want to use.

class UserForm(forms.ModelForm): #class name can be anything, arg must be same.
    class Meta: #class name must be same.
        model = userData #parameters must be model, fields.
        fields = ['email', 'name', 'password'] #pass any or all feilds of the model .
