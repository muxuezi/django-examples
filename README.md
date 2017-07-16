# Django Form Wizard Examples

> django-formtools Doc: https://django-formtools.readthedocs.io


### Environment

``` bash
$ virtualenv venv --python=python3.6
$ source venv/bin/activate

(venv) $ pip install -r requirements.txt
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

[Basic](example1-basic/)

[Custom template](example2-custom-template/)

[Different template](example3-different-template/)

[Handling files](example4-handling-files/)

[ModelForm](example5-modelform/)