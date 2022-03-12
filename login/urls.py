from django.urls import path
from .views import signupPage,loginPage,logout

urlpatterns = [
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logout, name='logout'),
]
