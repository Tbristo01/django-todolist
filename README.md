# Django-Todolist

[![License][license-image]][license-url] [![Build Status][travis-image]][travis-url]

Django-Todolist is a todolist web application with the most basic features of most web apps, i.e. accounts/login, API and (somewhat) interactive UI.

---
CSS | [Skeleton](http://getskeleton.com/)
JS  | [jQuery](https://jquery.com/)

I've also build a quite similar app in Flask: https://github.com/rtzll/flask-todolist

## Quick Start

1. **Install Python**: Download and install from [python.org](https://www.python.org/downloads/).
2. **Navigate**: Use `cd path/to/directory` in a terminal to navigate to `quick_start.py`.
3. **Run**: Execute with `python quick_start.py`.
4. **Observe**: Check the terminal for output.


## Explore
Try it out by installing the requirements. (Works only with python >= 3.8, due to Django 4)

    pip install -r requirements.txt

Migrate:

    python manage.py migrate

And then start the server (default: http://localhost:8000)

    python manage.py runserver


Now you can browse the [API](http://localhost:8000/api/)
or start on the [landing page](http://localhost:8000/)


[license-url]: https://github.com/rtzll/django-todolist/blob/master/LICENSE
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat

[travis-url]: https://travis-ci.org/rtzll/django-todolist
[travis-image]: https://travis-ci.org/rtzll/django-todolist.svg?branch=master
