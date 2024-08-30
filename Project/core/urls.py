from django.contrib import admin
from django.urls import path
from .views import *
from Project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CoreLoginView.as_view(), name="login"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)