from django.urls import path
from . import views

app_name = "strona"

urlpatterns = [
    path('', views.glowna, name="glowna"),
    path('dodaj/', views.dodaj_piosenke, name="dodaj_piosenke"),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('login/', views.zaloguj, name='login'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('piosenka/<int:piosenkaID>', views.informacje, name='informacje')
]