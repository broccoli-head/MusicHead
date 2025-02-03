from django.urls import path
from . import views

app_name = "strona"

urlpatterns = [
    path('', views.glowna, name="glowna"),
    path('dodaj/', views.dodaj_piosenke, name="dodaj_piosenke"),
]