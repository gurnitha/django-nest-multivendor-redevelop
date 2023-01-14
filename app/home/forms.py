# app/home/forms.py

# Import django modules
from django import forms
from django.utils.translation import gettext_lazy as _

# Import from locals
from app.home.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels = {'email':_('')}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'