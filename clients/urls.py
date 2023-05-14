from django.urls import path
from .views import home_screen_view,contact, home, success, fail

urlpatterns = [
    # path('', views.clients, name='clients'),
    path('', home_screen_view, name="home"),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('fail/', fail, name='fail'),
    # path('', home, name='home')

]