from django.urls import path
from .views import signupPage,loginPage,logout_user

urlpatterns = [
    path('signup_acc/', signupPage, name='signup'),
    path('login_acc/', loginPage, name='login'),
    path('logout_acc/', logout_user, name='logout'),
]
