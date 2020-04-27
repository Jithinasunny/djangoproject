from django.urls import path
from . import views

urlpatterns = [
    
    path('login',views.login,name='login'),
    path('',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('<id>/',views.customers,name='info'),
    path('review',views.chat,name='chat'),
    path('logout',views.logout,name='logout')
    

]