from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import logout
from .views import ( RegisterView, DashboardView,
                    LoginView, PhoneVerificationView,
<<<<<<< HEAD
                    IndexView,resend_url,view1,RestaurantView)
=======
                    IndexView,resend_url,view1)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
from django.contrib.auth import views as auth_views
from main.views import homepage
app_name='accounts'
urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index_page'),
    path('',homepage,name='homepage'),
    path('resend_url/<int:phone_number>/<int:country_code>',resend_url,name='resend_url'),
    url(r'^register/$', RegisterView.as_view(), name="register_url"),
    url(r'^login/$',view1, name="login_url"),
    url(r'^verify/$', PhoneVerificationView, name="phone_verification_url"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard_url"),
<<<<<<< HEAD
    url(r'^login_verify/$',LoginView,name="LoginView"),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^restaurant/$',RestaurantView,name='restaurant'),
=======
    url(r'^xyz/$',LoginView,name="LoginView"),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
]
