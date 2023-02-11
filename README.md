
# Django Blog Web Application

A full featured django application.


## Features
- User Singup, login and logout(Using the Django authentication system)
- An author can post the blog.
- Every blog has a category, author profile, publish date, and update date.
- The author can change their profile picture.
- Every user see the profile page, but only profile owner can update their profile information.

## Demo

![demo](https://github.com/rifatjamil54/Django-Blog-Site/blob/main/readme_img/django_demo.gif)


## Setup

* Clone my-project

```bash
git clone https://github.com/rifatjamil54/Django-Blog-Site.git
```

* Create and Activate virtual environment.

```bash
pip install virtualenv
virtualenv venv 
source venv/bin/activate
```

* Then following command-

```bash
cd Django-Blog-Web-Application/
pip install -r requirements.txt
```
* Go to project directory

```bash
cd blog_project/
```

* Migrate database

```bash
python manage.py makemigrations
python manage.py migrate
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

![App Screenshot](https://github.com/rifatjamil54/Django-Blog-Site/blob/main/readme_img/Screenshot%20from%202023-01-27%2012-50-59.png)



