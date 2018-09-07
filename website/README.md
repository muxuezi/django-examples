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

### Edit mirror

```
# Pipfile

- url = "https://pypi.org/simple"
+ url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

```
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
$ django-admin startproject example

$ cd example

$ python manage.py migrate
$ python manage.py runserver
```