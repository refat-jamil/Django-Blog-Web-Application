
# Django Blog Website

A full featured django application.


## Installation

Install my-project with git

```bash
git clone https://github.com/rifatjamil54/Django-Blog-Site.git
```

Create and Activate virtual environment.

Then following command-

```bash
pip install -r requirements.txt
```
Go to project directory

```bash
cd Django-Blog-Site/blog_root/
```

Migrate database

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py migrate --run-syncdb
```
Create superuser

```bash
python3 manage.py createsuperuser
```
Go to Django Admin Site create a Group name 'Author' and add these permissions.

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

Run server using
```bash
python3 manage.py runserver
```

