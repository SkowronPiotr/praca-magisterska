from django.urls import path, include

from . import views
from strona_glowna.views import KontaktView


urlpatterns = [
    path("strona_glowna/", views.index, name="strona_glowna",),
    path("kontakt/", KontaktView.as_view(), name="kontakt"),
    path("", views.wiadomosc, name="wiadomosc"),
    path("rejestracja/", views.rejestracja, name="rejestracja"),
    path("logowanie/", views.logowanie, name="logowanie"),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path("profil/", include('uzytkownik.urls')),
    path("wyszukiwanie/", views.wyszukiwanie, name="wyszukiwanie"),
    path("<int:Id_gatunku>", views.gatunek_detail, name="gatunek-detail"),
]
