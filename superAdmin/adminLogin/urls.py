from django.urls import path
from . import views


urlpatterns = [
    path('registerPage', views.registerPage, name='registerPage'),

    path('', views.loginPage, name='loginPage'),

    path('logout', views.logouts, name='logout'),
]