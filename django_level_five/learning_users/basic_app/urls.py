from django.urls import path
from basic_app import views

#template tagging

app_name='basic_app'

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path("register/",views.register,name='register'),
]