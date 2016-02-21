User Record API
################

A RESTful API for managing user records.

Developer Setup
================

Requirements:
    * Django 1.8+
    * djangorestframework 3.3+
    * Python 3.3+

This project uses SQLite: this is for demo & local testing purposes only, and
*not* intended for use in production.

A Python 3 virtualenv is recommended for local development.

Running
========

To install dependencies:
    ``(users)$ pip install -r requirements.txt``

To run the development server:
    ``(users)$ python manage.py runserver``


Testing
=========


Notes
======

* This is a demo project only: in the real world, a secure ``SECRET_KEY`` (for
  project-level ``settings.py``) value would be generated locally, and stored
  outside of the repo.
