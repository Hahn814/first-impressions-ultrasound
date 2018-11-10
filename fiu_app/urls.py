from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/<int:pk>/edit/', views.home_body_edit, name='home_body_edit'),
    path('packages', views.packages, name='packages'),
    path('packages/new/', views.package_new, name='package_new'),
    path('packages/<int:pk>/edit/', views.package_edit, name='package_edit'),
    path('packages/<int:pk>/remove/', views.package_remove, name='package_remove'),
    path('facilities', views.facilities, name='facilities'),
    path('galleries', views.galleries, name='galleries'),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact_us, name='contact_us'),
    path('gifts', views.gift_certificates, name='gift_certificates'),
    path('ad/new/', views.ad_new, name='ad_new'),
    path('ad/<int:pk>/edit/', views.ad_edit, name='ad_edit'),
    path('ad/<int:pk>/remove/', views.ad_remove, name='ad_remove'),
]
