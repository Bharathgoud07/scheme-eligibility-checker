from django.urls import path
from .views import documents_form

urlpatterns = [
    path('', documents_form, name='documents_form'),
]
