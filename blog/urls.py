from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
	path('register/', user_views.register, name='register'),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('services/', views.services, name='blog-services'),
    path('membership/', views.membership, name='blog-membership'),
    path('infocenter/', views.infocenter, name='blog-infocenter'),
    path('CSR/', views.CSR, name='blog-CSR'),
    path('contact/', views.contact, name='blog-contact'),

]
