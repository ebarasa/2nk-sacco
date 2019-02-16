from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('services/', views.services, name='blog-services'),
    path('membership/', views.membership, name='blog-membership'),
    path('infocenter/', views.infocenter, name='blog-infocenter'),
    path('CSR/', views.CSR, name='blog-CSR'),
    path('contact/', views.contact, name='blog-contact'),

]
