from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'department'}), required=False)
