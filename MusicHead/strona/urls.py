from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "strona"

urlpatterns = [
    path('', views.glowna, name="glowna"),
    path('dodaj/', views.dodaj_piosenke, name="dodaj_piosenke"),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('login/', views.zaloguj, name='login'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('piosenka/<int:piosenkaID>', views.informacje, name='informacje'),
    path('uzytkownik/<str:nazwaUzytkownika>', views.profil, name='profil')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)