from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('terms_and_condition', views.terms, name='terms'),
    path('signin',views.signin,name='login'),
    path('logout',views.Logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('deposit', views.deposit, name='deposit'),
    path('pay_view', views.pay_view, name='pay_view'),
    path('success/', views.success_view, name='payments-success'),
    path('cancel/', views.cancel_view, name='payments-cancel'),
    path('webhook/', views.coinbase_webhook),
    path('transaction_id', views.transaction_id, name='transaction_id'),
    path('deposit_update/<int:id>/', views.deposit_update, name='deposit_update'),
    path('deposit_table', views.deposit_table, name='deposit_table'),
    path('depositrecord', views.depositrecord, name='depositrecord'),
    path('withdrawrecord', views.withdrawrecord, name='withdrawrecord'),
    path('withdraw', views.withdrawals, name='withdraw'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='Change-password.html',
            success_url = '/reset_password_sent'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='Change-password-sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Change-password-new.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Change-password-finish.html'),name="password_reset_complete"),
    ]