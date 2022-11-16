from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name="register"),
    path('register/confirm', views.confirmregister, name='confirmregister'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),

]
