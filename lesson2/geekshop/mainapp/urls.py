from django.urls import path, include
from .views import index, contacts

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts)
]

