from django.urls import path
from . import views

urlpatterns = [
    path('', views.customerView.as_view(), name='customer'),
    path('<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail')
]
