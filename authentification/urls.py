from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login-card"),
    path('verification/', views.VerificationApi.as_view()),
]