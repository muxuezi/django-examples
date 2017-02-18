# Django Form Wizard Examples

> django-formtools Doc: https://django-formtools.readthedocs.io/


### Environment

``` bash
virtualenv venv --python=python3.5
source venv/bin/activate

(venv) pip install django
(venv) pip install django-formtools
```


### Installation app

``` python
# settings.py

INSTALLED_APPS = (
    # ...
    'formtools',
)
```


### Examples

- [x] [Basic](example1/)
- [x] [Custom template](example2/)
- [x] [Different template](example3/)
- [ ] Handling files
- [ ] ModelForm
