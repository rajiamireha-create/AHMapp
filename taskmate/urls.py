
from django.contrib import admin
from django.urls import path, include
from ahmadapp import views as ahmad_views

urlpatterns = [
    path('', ahmad_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('ahmadapp/',include('ahmadapp.url')),
    path('account/',include('user_app.url')),
    path('contact/',ahmad_views.contact, name='contact'),
    path('home/',ahmad_views.home, name='home'),
    path('features/',ahmad_views.features, name='features'),
    path('pricing',ahmad_views.pricing, name='pricing'),
    
    
]
