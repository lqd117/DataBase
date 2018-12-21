from django.urls import path

from . import views

app_name = 'research'
urlpatterns = [
    path('', views.index, name='index'),
    path('do_login/',views.do_login,name='do_login'),
    path('home/',views.home,name='home')
]