# Django Form Wizard Examples

> django-formtools Doc: https://django-formtools.readthedocs.io


### Environment

``` bash
$ virtualenv env --python=python3.6
$ source env/bin/activate

(env) $ pip install -r requirements.txt
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

- [Basic](example1-basic/)
- [Custom template](example2-custom-template/)
- [Different template](example3-different-template/)
- [Handling files](example4-handling-files/)
- [ModelForm](example5-modelform/)



### Links

- http://www.tivix.com/blog/django-form-wizard
- https://www.youtube.com/watch?v=fSnBF-BmccQ
- https://chriskief.com/2013/05/24/django-form-wizard-and-getting-data-from-previous-steps
- http://blog.hayleyanderson.us/2015/07/26/passing-information-between-django-form-wizard-steps
