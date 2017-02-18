# Using a different template for each form


### 0. [basic](../example1/) / [custom template](../example2/)


### 1. edit views

``` python
# contact/views.py

# ...

FORMS = [
    ('info', ContactForm1),
    ('message', ContactForm2),
]

TEMPLATES = {
    'info': 'contact_info.html',
    'message': 'contact_message.html'
}

class ContactWizard(SessionWizardView):
    # ...
```


### 2. edit urls

``` python
# urls.py

# ...

from contact.views import ContactWizard, FORMS

urlpatterns = [
    url(r'^contact/', ContactWizard.as_view(FORMS)),
    url(r'^done/', TemplateView.as_view(template_name='done.html')),
]
```
