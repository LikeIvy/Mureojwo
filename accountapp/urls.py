from django.urls import path
from accountapp.views import test

app_name = 'accountapp'

urlpatterns = [
    path('test/', test, name='test'),
]