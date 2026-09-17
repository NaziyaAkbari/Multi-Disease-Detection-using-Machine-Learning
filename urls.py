from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='disease_home'),
    path('tuberculosis/', views.tuberculosis_predict, name='tb_predict'),
    path('skin/', views.skin_predict, name='skin_predict'),
    path('malaria/', views.malaria_predict, name='malaria_predict'),
    path('asthma/', views.asthma_predict, name='asthma_predict'),
    path('chickenpox/', views.chickenpox_predict, name='chickenpox_predict'),
    path('history/', views.prediction_history, name='prediction_history'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]