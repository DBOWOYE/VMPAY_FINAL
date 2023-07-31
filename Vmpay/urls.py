from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', include("number_card.urls")),
    path('customer/', include("customer.urls"), name='customers'),
    path('account/', include("vmp_account.urls")),
    path('authentification/', include("authentification.urls")),
]
