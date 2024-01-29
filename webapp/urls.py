from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="homePage"),
    path('about/', views.about_page, name="aboutPage"),
    path('login/', views.login_page, name="loginPage"),
    path('how/', views.how_page, name="howPage"),
    path('browse/', views.browse_page, name="browsePage"),
    path('become/', views.become_page, name="becomePage"),
    path('sign-in/', views.signin_page, name="signinPage"),
]
