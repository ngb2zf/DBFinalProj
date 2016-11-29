from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class Hosts(models.Model):
	user = models.OneToOneField(User, unique=False)
	h_id = models.AutoField(primary_key=True)
	h_name = models.CharField(max_length=255)
	h_email = models.CharField(max_length=255)
	h_phone = models.CharField(max_length=31)
	h_availability = models.CharField(max_length=255)
	h_avgrating = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
 

class Bands(models.Model):
	user = models.OneToOneField(User, unique=False)
	b_id = models.AutoField(primary_key=True)
	b_name = models.CharField(max_length=255)
	b_email = models.CharField(max_length=255)
	b_phone = models.CharField(max_length=31)
	b_availability = models.CharField(max_length=255)
	b_avgrating = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
	b_price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
	b_bio = models.TextField()
	b_lat = models.DecimalField(max_digits=10, decimal_places=8)
	b_lon = models.DecimalField(max_digits=11, decimal_places=8)
	b_address = models.CharField(max_length=255)


class Events(models.Model):
	e_id = models.AutoField(primary_key=True)
	h_id = models.ForeignKey(Hosts, on_delete=models.CASCADE)
	b_id = models.IntegerField(blank=True, null=True)
	e_name = models.CharField(max_length=255)
	e_lat = models.DecimalField(max_digits=10, decimal_places=8)
	e_lon = models.DecimalField(max_digits=11, decimal_places=8)
	e_address = models.CharField(max_length=255)
	e_capac = models.IntegerField(blank=True, null=True)
	e_bandpaid = models.NullBooleanField()
	e_accepted = models.NullBooleanField()
	e_start = models.DateTimeField()
	e_end = models.DateTimeField()


