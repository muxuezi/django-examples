# Handling files


### 0. [basic](../example1/) / [custom template](../example2/) / [different template](../example3/)


### 1. add form and template

``` python
# contact/forms.py

# ...

class ContactForm3(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput)
```

``` python
# contact/views.py

# ...
from contact.forms import ContactForm1, ContactForm2, ContactForm3

FORMS = [
    # ...
    ('file', ContactForm3),
]

TEMPLATES = {
    # ...
    'file': 'contact_file.html'
}
```


### 2. add `multipart/form-data` to template

``` html
<!-- template/contact_file.html -->

<form enctype="multipart/form-data" action="" method="post">
```


### 3. add `file_storage` to WizardView subclass

``` python
# contact/views.py

# ...
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# ...

class ContactWizard(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'files_temp'))
    # ...
```


### 4. add `MEDIA_ROOT` to settings

``` python
# settings.py

# ...
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
