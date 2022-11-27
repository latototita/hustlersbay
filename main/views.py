from django.shortcuts import render, redirect , HttpResponseRedirect
from datetime import date
from datetime import datetime
from .models import Balance,Withdrawal,Deposit,Referred,ReferralBonu
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
import random

import logging
from coinbase_commerce.client import Client
from coinbase_commerce.error import SignatureVerificationError, WebhookInvalidPayload
from coinbase_commerce.webhook import Webhook
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from scumtrader import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail

from django.contrib.auth.hashers import make_password
#from .pay import PayClass 
# Create your views here.

def index(request):
    posts=Post.objects.all()
    today = datetime.date.today()
    timetoday=timezone.now
    results=request.GET.get("kw")
    if request.user.is_authenticated:
        if Balance.objects.filter(date_deposited__gte=today).filter(person=request.user.username):
            pass
        else:
            try:
                money_new_new=Balance.objects.get(person=request.user.username)
            except:
                money_new_new=None
            if money_new_new is None:
                pass
            else:
                print(money_new_new)
                money=float(money_new_new.amount)
                if  10<=money<=150:
                    money_new=(((4/100)*money)+money)
                    print(money_new)
                elif 151<=money<=350:
                    money_new=(((4.1/100)*money)+money)
                elif 351<=money<=750:
                    money_new=(((4.2/100)*money)+money)
                elif 751<=money<=1250:
                    money_new=(((4.3/100)*money)+money)
                elif 1251<=money<=2000:
                    money_new=(((4.4/100)*money)+money)
                elif 2001<=money<=3000:
                    money_new=(((4.412/100)*money)+money)
                else:
                    money_new=money
                print(money_new)
                money_new_new.amount=str(round(money_new, 1))
                print(money_new)
                money_new_new.date_deposited=datetime.datetime.today()
                money_new_new.save()
        try:
            balance=Balance.objects.get(person=request.user.username)
        except:
            balance=0
            percentage=0
        try:
            lists_of_top_withdraws=list(Withdrawal.objects.filter(status=True).order_by('-date_withdraw')[:12])
            lists_of_top_disposites=Deposit.objects.filter(status=True).order_by('-date_deposit')[:12]
            lists_of_top_balances=list(Balance.objects.filter().order_by('-date_deposited')[:12])
        except:
            lists_of_top_balances=[]
            lists_of_top_disposites=[]
            lists_of_top_withdraws=[]
        if balance==0:
            pass
        else:
            if float(balance.amount)>0:
                money=float(balance.amount)
                balance=balance.amount
                if  10<=money<=150:
                    percentage=4
                elif 151<=money<=350:
                    percentage=4.1
                elif 351<=money<=750:
                    percentage=4.2
                elif 751<=money<=1250:
                    percentage=4.3
                elif 1251<=money<=2000:
                    percentage=4.4
                elif 2001<=money<=3000:
                    percentage=4.412
                else:
                    percentage=0
        print(f'{request.user.id}')
        context={'percentage':percentage,'timetoday':timetoday,'lists_of_top_balances':lists_of_top_balances,'lists_of_top_disposites':lists_of_top_disposites,'lists_of_top_withdraws':lists_of_top_withdraws,'balance':balance,'header':'Balances of Top Investors'}
        return render(request, 'index.html',context)
    context={'posts':posts}
    return render(request, 'blog.html',context)


def terms(request):
    context={}
    return render(request, 'terms .html',context)

@login_required
def depositrecord(request):
    try:
        lists=Deposit.objects.filter(person=request.user)
    except:
        lists={}
    context={'lists':lists,'header':'Deposits Initiated Record'}
    return render(request, 'withdrawdepositrecord.html',context)

@login_required
def withdrawrecord(request):
    try:
        lists=Withdrawal.objects.filter(person=request.user)
    except:
        lists={}
    context={'lists':lists,'header':'Withdraws Initiated Record'}
    return render(request, 'withdrawdepositrecord.html',context)
@login_required
def withdrawals(request):
    if request.method=="POST":
        amount=request.POST.get('amount')
        address=request.POST.get('wallet')
        method=request.POST.get('method')
        method_new=Wallet.objects.get(id=method)
        txt_random= ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567893456789abcdefghijklmnopqrstuvwxyz') for _ in range(10)])
        balance=Balance.objects.get(person=request.user)
        balance=balance.amount
        balance=Balance.objects.get(person=request.user)
        balance_of_withdrawn=(float(balance.amount)-float(amount))
        balance.amount=balance_of_withdrawn
        balance.save()
        withdrawal=Withdrawal(address=address,wallet=method_new,person=request.user,amount=amount,txt_random=txt_random,date_withdraw=datetime.datetime.today())
        withdrawal.save()
        return redirect('index')
        '''
        try:
            withdrawamount=Deposit.objects.get(person=request.user)
        except:
            withdrawamount=None
        if withdrawamount:
            withdrawaldate=withdrawamount.date_deposit
            if withdrawaldate != None:
                try:
                    new_withdrawaldate=(date.today()-withdrawaldate)
                except:
                    new_withdrawaldate=0

        if new_withdrawaldate<6:
            if amount<=((25/100)*Balance):
                balance=Balance.objects.get(person=request.user.id)
                balance_of_withdrawn=(balance.amount-amount)
                balance.amount=balance_of_withdrawn
                balance.save()
                withdrawal=Withdrawal(address=address,wallet=method_new,person=request.user,amount=amount,txt_random=txt_random,date_withdraw=datetime.datetime.today())
                withdrawal.save()
                withdrawmoney = PayClass.withdrawmtnmomo(amount, currency, txt_random, phone, message)
                if withdrawmoney["response"]==200 or withdrawmoney["response"]==202:
                    CheckWithdrawStatus = PayClass.checkwithdrawstatus(withdrawmoney["ref"])
                    print(CheckWithdrawStatus["status"])
                    if CheckWithdrawStatus["status"]=="SUCCESSFUL":
                        print("Notification recieved")

                else:
                    print("Problem withdraw")
            else:
                messages.success(request, f'Please withdraw amount less than 25% of your current balance or Wait after 6 days from your last deosit to withdraw all your cash and profits')
        else:

            if amount_withdrawal<=((80/100)*Balance):
                balance=Balance.objects.get(person=request.user.id)
                balance_of_withdrawn=(balance.amount-amount)
                balance.amount=balance_of_withdrawn
                balance.save()
                withdrawal=Withdrawal(address=address,wallet=method_new,person=request.user,amount=amount,txt_random=txt_random,date_withdraw=datetime.datetime.today())
                withdrawal.save()
                withdrawmoney = PayClass.withdrawmtnmomo("50", "EUR", "1234laban", "+256776576547", "Laban")
                if withdrawmoney["response"]==200 or withdrawmoney["response"]==202:
                    CheckWithdrawStatus = PayClass.checkwithdrawstatus(withdrawmoney["ref"])
                    print(CheckWithdrawStatus["status"])
                    if CheckWithdrawStatus["status"]=="SUCCESSFUL":
                        print("Notification recieved")

                else:
                    print("Problem withdraw")
            else:
                pass
                a = date.today()
                b = date(2023, 12, 31)
                delta = b - a
                print(delta.days, "days left in this year")
                '''

    try:
        category=Wallet.objects.all()
    except:
        category=[]
    context={'category':category,'header':'Withdrawal Form','button':'WIthdraw'}
    return render(request,'with.html',context)
'''
@staff_member_required
def transaction_id(request):
    txt_random = request.session.get('txt_random_session')
    if not txt_random:
        messages.success(request, 'Please First fill in this Deposit Form')
        return redirect('deposit')
    print(txt_random)
    if request.method=="POST":
        transID=request.POST.get('transID')
        try:
            txt=Deposit.objects.get(txt_random=txt_random)
        except:
            return redirect('deposit')
        txt.transID=transID
        txt.save()
        messages.success(request, 'Deposit made Successfully, Account Balance shall be updated Soon')
        request.session['txt_random_session']=''
        return redirect('index')
    context={}
    return render(request, 'dep.html',context)
'''

@login_required
def deposit(request):
    if request.method=="POST":
        amount=request.POST.get('amount')
        date_deposit=datetime.datetime.today()
        txt_random= ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567893456789abcdefghijklmnopqrstuvwxyz') for _ in range(10)])
        request.session['txt_random_session'] = f'{txt_random}'
        request.session['amount'] = f'{amount}'
        request.session['date_deposit'] = f'{date_deposit}'
        request.session['request_user'] = f'{request.user}'
        '''callPay = PayClass.momopay(amount, currency, txt_random, phone, message)
                    if callPay["response"]==200 or callPay["response"]==202:
                        verify = PayClass.verifymomo(callPay["ref"])
                        print(verify["status"])
                        if verify["status"]=="SUCCESSFUL":
                            print('Notification sent')
        
                    else:
                        messages.success(response, f'Problem with the System')'''
        feed_back=Deposit(person=request.user,amount=amount,txt_random=txt_random,date_deposit=date_deposit)
        feed_back.save()
        return redirect('pay_view')
            
    try:
        category=Currencie.objects.all()
    except:
        category=[]
    
    context={'category':category,'header':'Deposit Form','button':'Deposit'}
    return render(request,'withdep.html',context)
# Create your views here.
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['customer'] = user.id
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                messages.success(request, f'Welcome, {username}.You have Signed In Successfully')
                return redirect('index')
        else:
            print('else')
            messages.success(request, 'Username or Password Incorrect!')
            context={}
            return render(request,'sign-in.html',context)
    print('nothing')
    context={}
    return render(request,'sign-in.html',context)

def signup(response):
    password=response.POST.get('password')
    username=response.POST.get('username')
    email=response.POST.get('email')
    ref_name=response.POST.get('refferral')
    if response.method=="POST":
            if User.objects.filter(email=email):
                messages.success(response, f'Email already in use, Please use a different Email')
                return render(response,'sign-up.html')
            if User.objects.filter(username=username):
                messages.success(response, f'Username already in use, Please use a different Username')
                return render(response,'sign-up.html')
            try:
                referral_code=User.objects.get(username=ref_name)
            except:
                messages.success(response, f'Wrong Referral Username,User Not Registered in This System.')
                return render(response,'sign-up.html')
            Referreds=Referred(personwhorefferred=referral_code,personrefferred=username)
            Referreds.save()
            form=User(username=username,password=make_password(password),email=email)
            form.save()
            messages.success(response, f'Successfully Registered,Please log into your Account to Make Orders')
            return redirect('login')

    context={}
    return render(response,'sign-up.html',context)


@login_required
def Logout(request):
    logout(request)
    messages.success(request, 'You have Signed Out Successfully')
    return redirect('index')
@staff_member_required
def deposit_update(request,id):
    user=Deposit.objects.get(id=id)
    request_user=User.objects.get(username=user.person)
    #if Deposit.objects.filter(person=request_user).filter(txt_random=txt_random).filter(date_deposit__gte=date_deposit).filter(amount=amount):
    try:
        balance=Balance.objects.get(person=request_user)
    except:
        balance=None
    print(balance)
    if balance is not None:
        print(balance)
        balances=(float(balance.amount)+float(user.amount))
        balance.amount=balances
        balance.save()
        print(balances)
    else:
        balance=Balance(person=request_user,amount=user.amount)
        balance.save()
    try:
        reffered=Referred.objects.get(personrefferred=request_user)
    except:
        reffered=None
    if reffered is not None:
        if reffered.paid==False:
            name=reffered.personwhorefferred
            payingUser=Balance.objects.get(person=name)
            bonus=((7/100)*float(user.amount))
            newbalance=(float(payingUser.amount)+float(bonus))
            refferalbonus=ReferralBonu(person=name,amount=bonus,paid=True)
            refferalbonus.save()
            payingUser.amount=newbalance
            payingUser.save()

    deposit=Deposit.objects.get(id=id)
    deposit.status=True
    deposit.save()
    return redirect('deposit_table')

@staff_member_required
def deposit_table(request):
    deposits= Deposit.objects.filter(status=False)
    context={'deposits':deposits}
    return render(request,'super.html',context)
@staff_member_required
def deposit_tabledone(request):
    deposits= Deposit.objects.filter(status=True)
    context={'deposits':deposits}
    return render(request,'super.html',context)





def pay_view(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'https://www.hustlersbay.online/'
    txt_random = request.session.get('txt_random_session')
    amount = request.session.get('amount')
    date_deposit = request.session.get('date_deposit')
    request_user = request.session.get('request_user')
    print(txt_random, amount, date_deposit, request_user)
    if not txt_random:
        return redirect('deposit')
    amount=str(amount)
    txt_random=str(txt_random)
    date_deposit=str(date_deposit)
    request_user=str(request_user)
    product = {
        'name': 'Hustlersbay',
        'description': 'Crytocurrency Deposit.',
        'local_price': {
            'amount': json.loads(amount),
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
        'metadata': {
            'amount':amount,
            'txt_random':txt_random,
            'date_deposit':date_deposit,
            'request_user':request_user,
        },
    }
    charge = client.charge.create(**product)
    request.session['txt_random_session']=''
    request.session['amount']=''
    request.session['date_deposit']=''
    request.session['request_user']=''
    return render(request, 'home.html', {
        'charge': charge,
    })


def success_view(request):
    messages.success(request, f'Deposit Made Successfully.Amount Balance will be updated Shortly')
    return redirect('index')


def cancel_view(request):
    messages.success(request, f'Deposit Cancelled Successfully.')
    return redirect('index')


@csrf_exempt
@require_http_methods(['POST'])
def coinbase_webhook(request):
    logger = logging.getLogger(__name__)

    request_data = request.body.decode('utf-8')
    request_sig = request.headers.get('X-CC-Webhook-Signature', None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)

        # List of all Coinbase webhook events:
        # https://commerce.coinbase.com/docs/api/#webhooks

        if event['type'] == 'charge:confirmed':
            logger.info('Payment confirmed.')
            amount = event['data']['metadata']['amount']
            txt_random = event['data']['metadata']['txt_random']
            date_deposit = event['data']['metadata']['date_deposit']
            request_user = event['data']['metadata']['request_user']
            send_mail('Deposit Made Successfully',
            f'{request_user} Has Just made a Deposit Successfully;\n Amount :{amount} \n Txt_random :{txt_random} \n Time :{date_deposit}',
            settings.EMAIL_HOST_USER,
            ['pearlmartbusinesses@gmail.com'],
            fail_silently = True,
            )
            '''if Deposit.objects.filter(person=request_user).filter(txt_random=txt_random).filter(date_deposit__gte=date_deposit).filter(amount=amount):
                try:
                    balance=Balance.objects.get(person=request_user)
                except:
                    balance=None
                print(balance)
                if balance is not None:
                    print(balance)
                    balances=(float(balance.amount)+float(amount))
                    balance.amount=balances
                    balance.save()
                    print(balances)
                else:
                    balance=Balance(person=request_user,amount=amount)
                    balance.save()
                try:
                    reffered=Referred.objects.get(personrefferred=request_user)
                except:
                    reffered=None
                if reffered is not None:
                    if reffered.paid==False:
                        name=reffered.personwhorefferred
                        payingUser=Balance.objects.get(person=name)
                        bonus=((7/100)*float(amount))
                        newbalance=(float(payingUser.amount)+float(bonus))
                        refferalbonus=ReferralBonu(person=name,amount=bonus,paid=True)
                        refferalbonus.save()
                        payingUser.amount=newbalance
                        payingUser.save()

                deposit=Deposit.objects.get(person=request_user)
                deposit.status=True
                deposit.save()'''

    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        return HttpResponse(e, status=400)

    logger.info(f'Received event: id={event.id}, type={event.type}')
    return HttpResponse('ok', status=200)
