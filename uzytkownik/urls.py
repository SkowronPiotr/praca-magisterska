from django.urls import path, reverse_lazy
from uzytkownik import views
# from django.views.generic import CreateView, UpdateView, DeleteView
from django.views import generic

from uzytkownik.views import NowyWpisUzytkownikaView, EdytujWpisUzytkownikaView, PanelUzytkownikaView
from .models import GatunekUzytkownika

app_name = 'uzytkownik'

urlpatterns = [
    path("", views.profil, name="profil"),
    path("nowy_wpis/", NowyWpisUzytkownikaView.as_view(), name="nowy_wpis"),
    # path("twoje_wpisy/", views.panel_uzytkownika, name="twoje_wpisy"),
    path("twoje_wpisy/", PanelUzytkownikaView.as_view(), name="twoje_wpisy"),
    path("porownaj/", views.porownaj_rekordy, name="porownaj"),
    path("<slug:slug>/", views.gatunek_uzytkownika_detail,
         name="gatunek-uzytkownika-detail"),
    path('<slug:slug>/delete/',
         generic.DeleteView.as_view(
             model=GatunekUzytkownika,
             success_url=reverse_lazy('uzytkownik:twoje_wpisy'),
             template_name='generic_delete.html'
         ),
         name='usun'),
    path("<slug:slug>/edytuj/", views.edytuj_wpis_uzytkownika, name="edytuj"),
    # path('<slug:slug>/edytuj/',
    #      UpdateView.as_view(
    #          model=GatunekUzytkownika,
    #          fields='__all__',
    #          success_url=reverse_lazy('uzytkownik:twoje_wpisy'),
    #          template_name='uzytkownik/edytuj_wpis.html'
    #      ),
    #      name='edytuj'),

]
