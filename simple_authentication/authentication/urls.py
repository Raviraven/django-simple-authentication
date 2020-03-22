from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('test', views.test_view, name='test')
]