from django.db import models
from django.utils import timezone

# Create your models here.
class Estimate(models.Model):
	id = models.AutoField(primary_key=True)
	salary = models.IntegerField()	
	age = models.IntegerField()
	summ = models.IntegerField()	
	time = models.IntegerField()
	experience = models.IntegerField()
	history = models.IntegerField()
	current = models.IntegerField()
	outstanding = models.IntegerField()


	
		
class Clients(models.Model):
	author = models.ForeignKey('auth.User')
	result = models.BooleanField()
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField('e-mail', blank=True)
	age = models.IntegerField()
	salary = models.IntegerField()
	childrens = models.BooleanField()
	job = models.BooleanField()
	experience = models.IntegerField(blank=True)
	amount_of_credit = models.IntegerField()
	payout_period = models.IntegerField()
	credits_history = models.IntegerField()
	number_of_current_credits = models.IntegerField()
	number_of_outstanding_credits = models.IntegerField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
"""
	def publish(self):
		self.published_date = timezone.now()
		self.save()
"""		

