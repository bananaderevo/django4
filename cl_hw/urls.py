from django.urls import path

from . import views

app_name = 'cl_hw'
urlpatterns = [
    path('', views.send, name='send'),

]