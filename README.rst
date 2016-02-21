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

From within the project's virtualenv, install dependencies:
    ``$ pip install -r requirements.txt``

Then run the development server:
    ``$ python manage.py runserver``

With the local dev server running, you can access the API via normal means,
e.g.,:
    ``$ curl localhost:8000/api/users``

You can also interactively browse the API & its documentation in your browser,
at
    ``localhost:8000/api/users`` and ``localhost:8000/api/groups``.

Testing
=========

To run tests, activate the project's virtualenv and do:

    ``$ python api/manage.py test users``

Notes
======

*This project is just a demo, and not intended for use in production.*

Some notes & points of consideration for "real world" application.

* secrets: in any other situation, a secure ``secret_key`` (for project-level
  ``settings.py``) value should be generated locally, and stored outside of the
  repo. Similarly, database and related credentials should be kept private.

* authentication: here, all CRUD actions are accessable by anonymous users:
  real-world use would want authentication for at least some actions
  implemented.

* updating groups: since the spec states an update to a group name consists of
  "a json list describing the group's members", and not a full group record,
  users may expect this to happen via PATCH instead of PUT.

* debug mode: For production, in ``settings.py``, **DEBUG** should be set to
  **FALSE**.
