# DBFinalProj
Book-a-Band DB final project


I realize there is a lot here and it took me awhile to set up, so if you have questions I can try and help if you are on Windows. If not I hope there is enough info in these tutorials that we can sort it out or I can try and help when we meet tommorrow.<br/>

I am using this guide to set up Django<br/>
https://docs.djangoproject.com/en/1.10/intro/install/<br/>
<br/>
You're going to want to have pip installed, should be with any python version >2.7<br/>
<br/>
I am using pycharm with python3.4<br/>
<br/>
1)Install Django with pip<br/>
From command prompt you want to type:<br/>
  $ pip install Django==1.10.3<br/>
To install the newest Django<br/>
https://www.djangoproject.com/download/<br/>
<br/>
2)Install and setup MYSQL<br/>
Install<br/>
http://dev.mysql.com/doc/refman/5.7/en/installing.html<br/>
Set-up info: You need to do this because you hardcode it into the settings file<br/>
  Port: 3306<br/>
  User: root<br/>
  PW: cs4750<br/>
<br/>
Make a schema called "bookaband" in the MYSQL Workbench (cylinder button on top left, "create new schema")<br/>
<br/>
Pay attention to this pip command:<br/>
  $ pip install mysqlclient==1.3.6<br/>
This is needed to connect Django to MySQL<br/>
<br/>
Tutorial for setting it all up - Don't worry about what they say about settings or ENV variables<br/>
http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-mysql-for-django<br/>


<br/>
-----------------------------------------------------------OTHER---------------------------------------------------------------
<br/>
Don't run from pycharm, it's easier to run from cmd because pycharm won't make migrations and migrate database.<br/>
<br/>
To runserver:<br/>
  python manage.py runserver<br/>
  View the site locally at http://127.0.0.1:8000/<br/>
<br/>
Making migrations<br/>
  Change your models (in models.py).<br/>
  Run python manage.py makemigrations to create migrations for those changes<br/>
  Run python manage.py migrate to apply those changes to the database.<br/>
  

