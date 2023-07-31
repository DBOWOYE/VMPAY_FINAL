from django.urls import path
from . import views
urlpatterns = [
    path('generate/', views.generate_number, name="generate"),
    path('', views.get_card_number, name = "cards"),
    
]