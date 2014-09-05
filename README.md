kawaldpr
========

A bootstrap-themed web application framework built on top of Django. The purpose of this framework is to make website 
development is easier. The specific goals are:

1. **Reducing development time** by implementing a lot of standard features
2. **Secure and stable** by implement pre-defined security features
3. **High performance** by setting performance tuning by default
 
 
It features are:

- Custom User model with email or username authentication
- Mandatory-boring-to-develop pages like sign in, sign up, contact, and reset password
- Admin page protection with django-admin-honeypot and admin log activity
- Assets pipelining with django-pipeline with jsmin and gzip compression for static files
- Twitter Bootstrap default integration

Quick Start
===========

If you want to start using the template, run this command::

    $ django-admin.py startproject --template=https://github.com/edwinlunando/arunafelt/archive/master.zip --extension=py,rst,html project_name
    
Change the `project_name` into your preference.

How to use
==========

Libraries
=========

In this section, I will explain the usage of every libraries that have been included in the application

Django
------

The main framework.

bpython
-------

bpython is an alternative interface from the standard python interpreter. It has auto complete feature and in-line 
syntax highlighting

django-braces
-------------

django-braces provides a lot of mixin class to help you to write clean code in Django class based views. Probably the 
most useful Mixin is `LoginRequiredMixin`
 
django-model-utils
------------------



This repo is in under heavy development!