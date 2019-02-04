from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('plivoterminal.urls')),
    path('babylon/inbound/sms/login/admin', admin.site.urls),
]

