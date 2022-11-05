from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"

class RegistrationForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=["username","email","password1","password2"]


class Withdrawal_Form_Customer(ModelForm):
	class Meta:
		model=Withdrawal
		fields=('amount',)
	amount = forms.CharField(required=True,label='Amount in Dollars eg.$10',)


class Withdrawal_Form_New(ModelForm):

	class Meta:
		model=Withdrawal
		fields=('amount','phone','currency')
	amount=forms.CharField(label='MTN Account Registration Name',required=False)
	#amount = forms.CharField(required=True,label='Amount in Dollars eg.$10',)
	phone = forms.CharField(required=True,label="Do not Put a plus Sign,eg.'256..','254'",)
'''
class Deposit_Form(forms.ModelForm):

	class Meta:
		model=Deposit
		fields=["amount","phone","currency"]
	amount=forms.CharField(label='Customize Your Own Category for Products',required=True)
	phone = forms.CharField(required=True)'''