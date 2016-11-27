# DBFinalProj
Book-a-Band DB final project


I realize there is a lot here and it took me awhile to set up, so if you have questions I can try and help if you are on Windows. If not I hope there is enough info in these tutorials that we can sort it out or I can try and help when we meet tommorrow.

I am using this guide to set up Django
https://docs.djangoproject.com/en/1.10/intro/install/

You're going to want to have pip installed, should be with any python version >2.7

I am using pycharm with python3.4

1)Install Django with pip
From command prompt you want to type:
  $ pip install Django==1.10.3
To install the newest Django
https://www.djangoproject.com/download/

2)Install and setup MYSQL
Install
http://dev.mysql.com/doc/refman/5.7/en/installing.html
Set-up info: You need to do this because you hardcode it into the settings file
  Port: 3306
  User: root
  PW: cs4750

Make a schema called "bookaband" in the MYSQL Workbench (cylinder button on top left, "create new schema")

Pay attention to this pip command:
  $ pip install mysqlclient==1.3.6
This is needed to connect Django to MySQL

Tutorial for setting it all up - Don't worry about what they say about settings or ENV variables
http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-mysql-for-django



-----------------------------------------------------------OTHER---------------------------------------------------------------
Don't run from pycharm, it's easier to run from cmd because pycharm won't make migrations and migrate database.

To runserver:
  python manage.py runserver
  View the site locally at http://127.0.0.1:8000/

Making migrations
  Change your models (in models.py).
  Run python manage.py makemigrations to create migrations for those changes
  Run python manage.py migrate to apply those changes to the database.
  

