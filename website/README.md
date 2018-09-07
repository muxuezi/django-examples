# Start a Django website

> Python 3.7.x  
> Django 2.1.x  


### Use pipenv

``` bash
$ brew install pipenv
```

### Init virtualenv

``` bash
$ pipenv install
```

### Edit mirror (if you need)

``` diff
# Pipfile

- url = "https://pypi.org/simple"
+ url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

``` diff
# Pipfile.lock

- "url": "https://pypi.org/simple",
+ "url": "https://pypi.tuna.tsinghua.edu.cn/simple",
```

### Install Django

``` bash
$ pipenv install django
```
### Run

``` bash
$ pipenv shell
```

``` bash
(env-name) $ django-admin startproject example

(env-name) $ cd example

(env-name) $ python manage.py migrate
(env-name) $ python manage.py runserver
```