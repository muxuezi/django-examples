# Django Custom User Examples


``` command
virtualenv env --python=python3.6
source env/bin/activate

pip install -r requirements.txt
```

``` command
python manage.py makemigrations accounts
python manage.py migrate
```


## 1. Extending the existing User model

- [Profile model](example1-profile/)
- [Profile model: auto create](example2-profile-auto-create/)
- [Profile model: auto save](example3-profile-auto-save/)


## 2. Substituting a custom User model

- [AbstractUser](example4-AbstractUser/)
- [AbstractBaseUser](example5-AbstractBaseUser/)


## 3. Proxy model

- [example](example6-proxy/)
