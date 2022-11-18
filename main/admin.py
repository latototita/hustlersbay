from django.contrib import admin
from .models import *
# Register your models here.
class AdminCurrency(admin.ModelAdmin):
    list_display = ['name']
class AdminBalance(admin.ModelAdmin):
    list_display = ['person']

class AdminWithdrawal(admin.ModelAdmin):
    list_display = ['person']

class AdminReferred(admin.ModelAdmin):
    list_display = ['personwhorefferred']
class AdminDeposit(admin.ModelAdmin):
    list_display = ['person']

class AdminReferralBonus(admin.ModelAdmin):
    list_display = ['person']
class AdminPost(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Post, AdminPost)
admin.site.register(Balance, AdminBalance)
admin.site.register(Currencie, AdminCurrency)
admin.site.register(Withdrawal , AdminWithdrawal)
admin.site.register(Referred, AdminReferred )
admin.site.register(Deposit,AdminDeposit )
admin.site.register(ReferralBonu, AdminReferralBonus)