
# Django Blog Website

A full featured django application.


## Installation

* Install my-project with git

```bash
git clone https://github.com/rifatjamil54/Django-Blog-Site.git
```

* Create and Activate virtual environment.
* 
``bash
pip install virtualenv
virtualenv venv 
source venv/bin/activate
```

* Then following command-

```bash
pip install -r requirements.txt
```
* Go to project directory

```bash
cd Django-Blog-Site/blog_root/
```

* Migrate database

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py migrate --run-syncdb
```
* Create superuser

```bash
python3 manage.py createsuperuser
```

* Run server using
```bash
python3 manage.py runserver
```

* Go to Django Admin Site create a Group name 'Author' and add these permissions.

![App Screenshot](https://github.com/rifatjamil54/Django-Blog-Site/blob/main/Screenshot%20from%202023-01-27%2012-50-59.png)



