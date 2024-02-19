from django.urls import path
from uzytkownik import views

from uzytkownik.views import NowyWpisUzytkownikaView, EdytujWpisUzytkownikaView

app_name = 'uzytkownik'

urlpatterns = [
    path("", views.profil, name="profil"),
    path("nowy_wpis/", NowyWpisUzytkownikaView.as_view(), name="nowy_wpis"),
    path("twoje_wpisy/", views.panel_uzytkownika, name="twoje_wpisy"),
    path("porownaj/", views.porownaj_rekordy, name="porownaj"),
    path("<slug:slug>/", views.gatunek_uzytkownika_detail,
         name="gatunek-uzytkownika-detail"),
    path("<slug:slug>/delete/", views.usun, name="usun"),
    path("<slug:slug>/edytuj/", views.edytuj_wpis_uzytkownika, name="edytuj"),

]
