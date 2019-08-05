from django.conf.urls import url
from .import views
from django.urls import path

urlpatterns=[
path('list/', views.my_expense, name='cost-list'),
]