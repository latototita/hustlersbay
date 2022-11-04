from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from datetime import date
import datetime

class Balance(models.Model):
	person = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	amount= models.CharField(max_length=12)
	date_deposited =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_deposited', )

class Currencie(models.Model):
	name = models.CharField(max_length=12)
	def __str__(self):
		return self.name
class Withdrawal(models.Model):
	person = models.CharField(max_length=12,unique=True)
	date_withdraw =models.DateTimeField(default=datetime.datetime.today)
	amount= models.CharField(max_length=12)
	currency=models.ForeignKey(Currencie, on_delete=models.CASCADE, default=1)
	phone =models.CharField(max_length=12, default=1)
	txt_random=models.CharField(max_length=12,default=1)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_withdraw', )
class Deposit(models.Model):
	person = models.CharField(max_length=12,unique=True)
	date_deposit =models.DateTimeField(default=datetime.datetime.today)
	amount= models.CharField(max_length=12)
	currency=models.ForeignKey(Currencie, on_delete=models.CASCADE, default=1)
	phone =models.CharField(max_length=12, default=1)
	txt_random=models.CharField(max_length=12, default=1)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_deposit', )

class Earning(models.Model):
	person = models.CharField(max_length=12,unique=True)
	amount= models.CharField(max_length=15)
	time_earned =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-time_earned', )

class Referred(models.Model):
	personwhorefferred = models.CharField(max_length=12,unique=True)
	personrefferred= models.CharField(max_length=25, unique=True)
	date_refferred =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.personwhorefferred

	class Meta:
		ordering = ('-date_refferred', )

class ReferralBonu(models.Model):
	person = models.CharField(max_length=12,unique=True)
	paid= models.BooleanField(default=False)
	date_pained =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_pained', )