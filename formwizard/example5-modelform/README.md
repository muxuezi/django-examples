# ModelForm


### 0. [basic](../example1-basic/) / [custom template](../example2-custom-template/) / [different template](../example3-different-template/) / [handling template](../example4-handling-files/)


### 1. add model

``` python
# contact/models.py

from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    files = models.FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.subject
```


### 2. edit form

``` python
# contact/forms.py

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
```


### 3. save data

``` python
# contact/views.py

# ...

class ContactWizard(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'files_temp'))
    instance = None

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_instance(self, step):
        """
        get ModelForm
        """
        if self.instance is None:
            self.instance = Contact()
        return self.instance

    def done(self, form_list, **kwargs):

        self.instance.save() # save data

        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
```


### 4. commit

[84fd26c](https://github.com/mittya/django-formwizard-examples/commit/84fd26c26f148809aaeba1907e5849e6fa470cee)
