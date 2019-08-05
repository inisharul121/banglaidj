from django.conf.urls import url
from django.urls import path
from .import views
urlpatterns =[

    path('info/', views.show_user_info, name='user-info'),

]