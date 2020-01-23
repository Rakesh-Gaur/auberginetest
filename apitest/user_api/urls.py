from django.conf.urls import url, include
from allauth.account.views import ConfirmEmailView
from . import views

urlpatterns = [
    url('register', views.UserCreate.as_view(), name='register-user'),
    url('saveurl', views.save_url_image, name='Save-imageurl'),
    url(r'^registration/account-email-verification-sent/', views.error_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', views.verified_view, name='account_confirm_complete'),
    url(r'', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
]