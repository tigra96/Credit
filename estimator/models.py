from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.
class Estimate(models.Model):
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=20, null=True)
	Second_Name = models.CharField(max_length=20, null=True)
	Last_Name = models.CharField(max_length=20, null=True)
	birth = models.DateField(blank=True, null=True)
	passport = models.PositiveIntegerField(null=True)
	Amount = models.PositiveIntegerField(null=True)
	Salary = models.PositiveIntegerField(null=True)
	Work_Experience = models.PositiveIntegerField(null=True)
	Repayment_Period = models.PositiveIntegerField(null=True)
	
class LogIn(models.Model):
	Username = models.CharField(max_length=20)
	Password = models.CharField(max_length=20)

class surname(models.Model):
	surname  = models.CharField(max_length=20)
	
		
class client_info(models.Model):
	Id = models.AutoField(primary_key=True)
	id_author = models.IntegerField(null=True)
	second_name = models.CharField(max_length=20, null=True)
	first_name = models.CharField(max_length=20, null=True)
	third_name = models.CharField(max_length=20, null=True)
	birth = models.DateField(default=timezone.now)
	passport = models.IntegerField(null=True)
	email = models.EmailField(blank=True, null=True)
	
	
class client_history(models.Model):
	Id = models.AutoField(primary_key=True)
	Id_client = models.IntegerField(blank=True)
	start_credit = models.DateField(blank=True, null=True)
	finish_credit = models.DateField(blank=True, null=True)
	amount = models.IntegerField(blank=True)
	number_of_delays = models.IntegerField(blank=True)
	status = models.CharField(max_length=20, null=True)
	
class client_job(models.Model):
	Id = models.AutoField(primary_key=True)
	id_client = models.IntegerField(blank=True)
	work_place = models.CharField(max_length=20, null=True)
	salary = models.IntegerField(null=True)
	experience = models.IntegerField(null=True)

