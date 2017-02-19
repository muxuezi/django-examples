from django import forms

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=False)

class ContactForm3(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput)
