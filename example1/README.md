# Basic


### 1. add app

``` bash
cd example1

python manage.py startapp contact
```


### 2. defing form classes

``` python
# contact/forms.py

from django import forms

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
```


### 3. creating a `WizardView` subclass

``` python
# contact/views.py

from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

class ContactWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
```


### 4. add template

``` html
<!-- templates/done.html -->

<h1>Done</h1>

<div>
  {{ form_data }}
</div>
```

``` python
# settings.py

TEMPLATES = [
    {
        # ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ...
    },
]
```


### 5. add url

``` python
# urls.py

from django.conf.urls import url

from contact.forms import ContactForm1, ContactForm2
from contact.views import ContactWizard

urlpatterns = [
    url(r'^contact/', ContactWizard.as_view([ContactForm1, ContactForm2])),
]
```


### 6. run

``` bash
python manage.py migrate

python manage.py runserver
```

open `http://127.0.0.1:8000/contact`
