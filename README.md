# Django Form Wizard Examples

> django-formtools Doc: https://django-formtools.readthedocs.io/


### Environment

``` bash
$ virtualenv venv --python=python3.6
$ source venv/bin/activate

(venv) $ pip install django
(venv) $ pip install django-formtools
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

- [x] [Basic](example1-basic/)
- [x] [Custom template](example2-custom-template/)
- [x] [Different template](example3-different-template/)
- [x] [Handling files](example4-handling-files/)
- [x] [ModelForm](example5-modelform/)
