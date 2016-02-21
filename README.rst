User Record API
################

A RESTful API for managing user records.

Developer Setup
================

Requirements:
    * Django 1.8+
    * djangorestframework 3.3+
    * Python 3.4+

This project uses SQLite: this is for demo & local testing purposes only, and
*not* intended for use in production.

A Python virtualenv is recommended for local development:

``$ virtualenv --python python3.4 env``

Running
========

Activate the project's virtualenv:

``$ source env/bin/activate``

With the virtualenv active, install dependencies:

``$ pip install -r requirements.txt``

The first time you run the service locally, you'll need to setup the local
database schema:

``$ python manage.py migrate``

Once that's complete, you can run the development server:

``$ python manage.py runserver``

Usage & Testing
=================

With the local dev server running, you can access the API via normal means,
e.g.,:

``$ curl localhost:8000/api/users``

You can also interactively browse the API & its documentation in your browser,
at
``localhost:8000/api/users`` and ``localhost:8000/api/groups``.

To run the tests, use Tox. If Tox is not already installed, you can install it
with: 

``$ pip install tox``

(For more info on Tox, or help installing, `see here <http://tox.readthedocs.org/en/latest/>`_)

With Tox installed, from within the project root do:

``$ tox``

Notes
======

*This project is just a demo, and not intended for use in production.*

Some notes & points of consideration for "real world" application.

* secrets: in any other situation, a secure ``SECRET_KEY`` (for project-level
  ``settings.py``) value should be generated locally, and stored outside of the
  repo. Similarly, database and related credentials should be kept private.

* authentication: here, all CRUD actions are accessible by anonymous users:
  real-world use would want authentication for at least some actions
  implemented.

* updating groups: since the spec states an update to a group name consists of
  "a json list describing the group's members", and not a full group record,
  some users may expect this to happen via PATCH instead of PUT.

* debug mode: For production, in ``settings.py``, **DEBUG** should be set to
  **FALSE**. This will also require properly configuring & deploying static
  files (specifics depend on production setup) 
