from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login, logout

from .forms import FormularzRejestracji, FormularzLogowania
from .models import Kategorie, Gatunek, DaneSkladuChemicznego, DaneWlasciwosciFizycznych, DaneWlasciwosciMechanicznych, Komentarze
from uzytkownik.models import GatunekUzytkownika


def gatunek_detail(request, Id_gatunku):
    """
    It's a view for a record from one of the model. 
    It gets the element by primary key, and by process I have created shows up values user wants to see
    I will go through one of the property rest (chemical composition) is done same way
    for mechanical properties firstly program identifies record by primary key
    later it takes the to_dict method from model where are displayed mechanical properties
    next I create a a dictionary and display it on html
    """
    gatunek = get_object_or_404(Gatunek, pk=Id_gatunku)
    fizyczne = DaneWlasciwosciFizycznych.objects.get(pk=Id_gatunku)
    mechaniczne = DaneWlasciwosciMechanicznych.objects.get(pk=Id_gatunku)
    mechaniczne_dict = mechaniczne.to_dict_mechaniczne()
    wl_mechaniczne = {klucz: wartosc for klucz,
                      wartosc in mechaniczne_dict.items() if wartosc is not None}
    komentarze = Komentarze.objects.get(pk=Id_gatunku)
    sklad_chemiczny = DaneSkladuChemicznego.objects.get(pk=Id_gatunku)
    sklad_chemiczny_dict = sklad_chemiczny.to_dict_sklad_chemiczny()
    nowy_sklad_chemiczny = {klucz: wartosc for klucz,
                            wartosc in sklad_chemiczny_dict.items() if wartosc is not None}
    return render(request, "strona_glowna/gatunek_detail.html", {
        'gatunek': gatunek,
        'fizyczne': fizyczne,
        'komentarze': komentarze,
        'sklad_chemiczny': nowy_sklad_chemiczny,
        'wl_mechaniczne': wl_mechaniczne,
    })


def wyszukiwanie(request):
    """
    View for searching page, you can search by a name, category, comment,
    """
    kategorie = Kategorie.objects.all()
    query = request.GET.get('query', '')
    gatunki = Gatunek.objects.all()
    gatunki_uzytkownika = GatunekUzytkownika.objects.all()
    komentarze = Komentarze.objects.all()
    kategoria_id = request.GET.get('kategoria', 0)

    if kategoria_id:
        gatunki = gatunki.filter(kategoria_id=kategoria_id)
        gatunki_uzytkownika = gatunki_uzytkownika.filter(
            kategoria_id=kategoria_id)

    if query:
        gatunki = gatunki.filter(Q(gatunek__icontains=query))
        gatunki_uzytkownika = gatunki_uzytkownika.filter(
            Q(nazwa__icontains=query))

    if query:
        komentarze = komentarze.filter(
            Q(Komentarz__icontains=query) | Q(Aplikacje__icontains=query))

    return render(request, 'strona_glowna/wyszukiwanie.html', {
        'gatunki': gatunki,
        'gatunki_uzytkownika': gatunki_uzytkownika,
        "komenarze": komentarze,
        'query': query,
        "kategorie": kategorie,
        'kategoria_id': int(kategoria_id),
        'is_szukaj_active': True,
    })


def index(request):
    """
    Basic view for main page, with counter and parameter for styling
    """
    admin_model = Gatunek.objects.count()
    uzytkownik_model = GatunekUzytkownika.objects.count()
    suma = admin_model + uzytkownik_model
    return render(request, 'strona_glowna/index.html', {
        'is_index_active': True,
        "suma": suma,
    })


def wiadomosc(request):
    """
    I wanted to create a welcome message that shows up only one time per session
    Currently it doesn't work as planned I will update it
    """
    # # Sprawdź, czy sesja już istnieje
    # if 'new_user' not in request.session:
    #     # Jeżeli nie, oznacz użytkownika jako nowego
    #     request.session['new_user'] = True
    # else:
    #     # Jeżeli sesja już istnieje, oznacz użytkownika jako nie-nowego
    #     request.session['new_user'] = False

    return render(request, 'strona_glowna/wiadomosc.html')
 #                 , {'new_user': request.session['new_user']})


class KontaktView(TemplateView):
    """
    Basic view for Contact page, with counter and parameter for styling
    """
    template_name = 'strona_glowna/kontakt.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_kontakt_active = True
        context["is_kontakt_active"] = is_kontakt_active
        return context


def rejestracja(request):
    """
    Registration page
    """
    if request.method == "POST":
        formularz = FormularzRejestracji(request.POST)

        if formularz.is_valid():
            formularz.save()
            return redirect("/logowanie")
    else:
        formularz = FormularzRejestracji()

    return render(request, "strona_glowna/rejestracja.html", {
        'formularz': formularz,
    })


def logowanie(request):
    """
    Log in page
    """
    if request.method == 'POST':
        formularz = FormularzLogowania(request, data=request.POST)
        if formularz.is_valid():
            user = formularz.get_user()
            login(request, user)
            return redirect('strona_glowna')
    else:
        formularz = FormularzLogowania()

    return render(request, "strona_glowna/login.html", {
        'formularz': formularz,
        'is_login_active': True,
    })


@login_required
def wyloguj(request):
    """
    Log out page
    """
    logout(request)
    return redirect('/logowanie/')
