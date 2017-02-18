# Use custom template


### 0. [basic](../example1/)


### 1. add template

``` html
<!-- base.html -->

<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Form Wizard Example</title>
  <style>
    .wrapper {
      width: 600px;
      margin: 100px auto;
      padding: 20px;
      background-color: #f3f3f3;
      border-radius: 10px;
    }
  </style>
  {% block head %}{% endblock %}
</head>

<body>
    <div class="wrapper">
      {% block content %}{% endblock %}
    </div>
</body>
</html>
```

``` html
<!-- contact.html -->

{% extends "base.html" %}
{% load i18n %}

{% block head %}
{{ wizard.form.media }}
{% endblock %}

{% block content %}
<p>Step {{ wizard.steps.step1 }} of {{ wizard.steps.count }}</p>

<form action="" method="post">
  {% csrf_token %}
  <table>
  {{ wizard.management_form }}

  {% if wizard.form.forms %}
    {{ wizard.form.management_form }}
    {% for form in wizard.form.forms %}
      {{ form }}
    {% endfor %}
  {% else %}
    {{ wizard.form }}
  {% endif %}
  </table>

  {% if wizard.steps.prev %}
  <button name="wizard_goto_step" type="submit" value="{{ wizard.steps.first }}">{% trans "first step" %}</button>
  <button name="wizard_goto_step" type="submit" value="{{ wizard.steps.prev }}">{% trans "prev step" %}</button>
  {% endif %}

  <input type="submit" value="{% trans "submit" %}">
</form>
{% endblock %}
```


### 2. use template

``` python
# contact/views.py

# ...

class ContactWizard(SessionWizardView):
    template_name = 'contact.html'

    def done(self, form_list, **kwargs):
        # ...
```


### 3. keep the `urls.py` clean

``` python
# contact/views.py

from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

from contact.forms import ContactForm1, ContactForm2

class ContactWizard(SessionWizardView):
    template_name = 'contact.html'
    form_list = [ContactForm1, ContactForm2]

    def done(self, form_list, **kwargs):
        # ...
```

``` python
# urls.py

from django.conf.urls import url

from contact.views import ContactWizard

urlpatterns = [
    url(r'^contact/', ContactWizard.as_view()),
]

```
