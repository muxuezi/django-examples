from django import forms

from .models import Contact

class ContactForm1(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('subject', 'sender',)
        widgets = {
            'subject': forms.TextInput(),
            'sender': forms.EmailInput()
        }

class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('message',)
        widgets = {
            'message': forms.Textarea()
        }

class ContactForm3(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('files',)
        widgets = {
            'message': forms.ClearableFileInput()
        }
