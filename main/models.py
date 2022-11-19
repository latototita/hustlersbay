from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from datetime import date
import datetime

class Balance(models.Model):
	person = models.CharField(max_length=1000)
	amount= models.CharField(max_length=1000)
	date_deposited =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.amount

	class Meta:
		ordering = ('-date_deposited', )

class Currencie(models.Model):
	name = models.CharField(max_length=1000)
	def __str__(self):
		return self.name
class Withdrawal(models.Model):
	person = models.CharField(max_length=1000)
	date_withdraw =models.DateTimeField(default=datetime.datetime.today)
	amount= models.CharField(max_length=1000)
	method=models.ForeignKey(Currencie, on_delete=models.CASCADE, default=1)
	phone =models.CharField(max_length=1000, default=1)
	txt_random=models.CharField(max_length=1000,default=1)
	status=models.BooleanField(default=False)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_withdraw', )
class Deposit(models.Model):
	person = models.CharField(max_length=1000)
	amount= models.CharField(max_length=1000)
	method=models.ForeignKey(Currencie, on_delete=models.CASCADE, default=1)
	wallet =models.CharField(max_length=1000, default=1)
	transID =models.CharField(max_length=1000, default=1)
	txt_random=models.CharField(max_length=1000, default=1)
	date_deposit =models.DateTimeField(default=datetime.datetime.today)
	status=models.BooleanField(default=False)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_deposit', )

class Earning(models.Model):
	person = models.CharField(max_length=1000)
	amount= models.CharField(max_length=15)
	time_earned =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-time_earned', )

class Referred(models.Model):
	personwhorefferred =  models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	personrefferred= models.CharField(max_length=1000)
	date_refferred =models.DateTimeField(default=datetime.datetime.today)
	paid=models.BooleanField(default=False)
	def __str__(self):
		return self.personrefferred

	class Meta:
		ordering = ('-date_refferred', )

class ReferralBonu(models.Model):
	person = models.CharField(max_length=1000,default=0)
	amount= models.CharField(max_length=1000,default=12)
	paid= models.BooleanField(default=False)
	date_pained =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_pained', )

class Post(models.Model):
    image=models.ImageField(upload_to='posts',blank=True)
    title = models.CharField(max_length=1000,default='None')
    link = models.CharField(max_length=1000,default='None')
    content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.datetime.today)

    class Meta:
        ordering = ('-date_posted', )

    def __str__(self):
        return self.title
