from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Quote, Author, Tag

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Quote'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Tags (existing only)'}),
        }