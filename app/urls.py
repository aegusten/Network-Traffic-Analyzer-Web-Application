from django.urls import path
from . import views

urlpatterns = [
    path('generate-pcap/', views.generate_pcap, name='generate_pcap'),
    path('upload-pcap/', views.upload_pcap, name='upload_pcap'),
    path('analyze-pcap/', views.analyze_pcap, name='analyze_pcap'),
    path('', views.home, name='home'),
]
