from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from uzytkownik.forms import GatunekUzytkownikaForm
from uzytkownik.models import GatunekUzytkownika

from praca_magisterska.funkcje import get_plot, get_bar_plot


def gatunek_uzytkownika_detail(request, slug):
    """
    View displays detailed page for user's record, it is made on a diffrent model
    methods are similar if not the same to display data
    chemical composition is taken from to_dict function made in models.py
    next I am creating a dictionary with a element and it's value
    and displaying it on page
    Filtered chemical composition is for chart 
    (I had a problem that it didn't display because there were empty values, this method deletes empty keys and values so chart can be created)
    Chart is created in funkcje.py
    Diffrences about models are commented in models.py
    query is for comparising reason, django takes this pk and displays it in compare page but you have to select other record to compare
    """
    gatunek = get_object_or_404(GatunekUzytkownika, slug=slug)
    query = gatunek.pk
    sklad_chemiczny = gatunek.to_dict_sklad_chemiczny()
    nowy_sklad_chemiczny = {klucz: wartosc for klucz,
                            wartosc in sklad_chemiczny.items() if wartosc is not None}
    filtered_sklad_chemiczny = {key: value for key, value in sklad_chemiczny.items(
    ) if value is not None and value != 0}
    mechaniczne = gatunek.to_dict_mechaniczne()
    filtered_mechaniczne = {klucz: wartosc for klucz,
                            wartosc in mechaniczne.items() if wartosc is not None}
    wykres_mechaniczne_labels = list(filtered_mechaniczne.keys())
    wykres_mechaniczne = list(filtered_mechaniczne.values())
    wl_mechaniczne = {klucz: wartosc for klucz,
                      wartosc in mechaniczne.items() if wartosc is not None}
    pierwiastki = list(filtered_sklad_chemiczny.keys())
    zawartosc = list(filtered_sklad_chemiczny.values())
    wykres_pierwiastkow = get_plot(zawartosc, pierwiastki)
    wykres_mechaniczny = get_bar_plot(
        wykres_mechaniczne_labels, wykres_mechaniczne)

    return render(request, "uzytkownik/gatunek_uzytkownika_detail.html", {
        "gatunek": gatunek,
        "sklad_chemiczny": nowy_sklad_chemiczny,
        "wl_mechaniczne": wl_mechaniczne,
        "query": query,
        "wykres_pierwiastkow": wykres_pierwiastkow,
        "wykres_mechaniczny": wykres_mechaniczny,
    })


def porownaj_rekordy(request):
    """
    Page for record comparison, currently on my page you can compare ONLY records made by user,
    Because it is done by one single model, so it was easier for me to display whole data
    user uses 2 queries to display 2 records he wants to compare
    licznik (counter) parameter has been created for a reason to cover a view when nothing is selected
    I had a problem when with empty queries you could see all records
    with my trick when you didn't sellect anything web displays a warning to actually sellect something
    Data is displayed same method from detail page
    """
    rekordy = GatunekUzytkownika.objects.all()
    wynik1 = GatunekUzytkownika.objects.all()
    wynik2 = GatunekUzytkownika.objects.all()
    query1 = request.GET.get('query1', '')
    query2 = request.GET.get('query2', '')
    sklad_chemiczny_list1 = None
    wl_mechaniczne1 = None
    sklad_chemiczny_list2 = None
    wl_mechaniczne2 = None
    licznik = wynik1.count()

    if query1:
        wynik1 = GatunekUzytkownika.objects.filter(pk=query1)
        sklad_chemiczny_list1 = [result.to_dict_sklad_chemiczny()
                                 for result in wynik1]
        wl_mechaniczne1 = [result.to_dict_mechaniczne()
                           for result in wynik1]
        licznik = 0

    if query2:
        wynik2 = GatunekUzytkownika.objects.filter(pk=query2)
        sklad_chemiczny_list2 = [result.to_dict_sklad_chemiczny()
                                 for result in wynik2]
        wl_mechaniczne2 = [result.to_dict_mechaniczne()
                           for result in wynik2]
        licznik = 0

    return render(request, 'uzytkownik/porownaj.html', {
        "rekordy": rekordy,
        "wynik1": wynik1,
        "wynik2": wynik2,
        "sklad_chemiczny_list1": sklad_chemiczny_list1,
        "wl_mechaniczne1": wl_mechaniczne1,
        "sklad_chemiczny_list2": sklad_chemiczny_list2,
        "wl_mechaniczne2": wl_mechaniczne2,
        "licznik": licznik,
    })


class Profil(LoginRequiredMixin, generic.DetailView):
    template_name = 'uzytkownik/profil.html'
    model = User
    # context_object_name = 'uzytkownik'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_profile_active'] = True
        return context


class PanelUzytkownikaView(generic.ListView):
    """
    Page for user to see list of records he created, he can edit them or delete,
    """
    model = GatunekUzytkownika
    template_name = "uzytkownik/twoje_wpisy.html"
    # paginate_by = 10
    # to be added

    def get_queryset(self):
        return super().get_queryset().filter(stworzony_przez=self.request.user)


def edytuj_wpis_uzytkownika(request, slug):
    """
    View for editing user's record
    """
    rekord = get_object_or_404(
        GatunekUzytkownika, slug=slug, stworzony_przez=request.user)
    if request.method == "POST":
        formularz = GatunekUzytkownikaForm(request.POST, instance=rekord)
        if formularz.is_valid():
            formularz.save()
            return redirect("uzytkownik:twoje_wpisy")
    else:
        formularz = GatunekUzytkownikaForm(instance=rekord)
    return render(request, "uzytkownik/edytuj_wpis.html", {
        "formularz_gestosci": formularz,
    })


class EdytujWpisUzytkownikaView(View):
    """
    alternative class View for editing user's record
    """

    def get(self, request, slug):
        rekord = get_object_or_404(
            GatunekUzytkownika, slug=slug, stworzony_przez=request.user)
        context = {
            "formularz_gestosci": GatunekUzytkownikaForm(instance=rekord),
        }
        return render(request, "uzytkownik/edytuj_wpis.html", context)

    def post(self, request, slug):
        rekord = get_object_or_404(
            GatunekUzytkownika, slug=slug, stworzony_przez=request.user)
        formularz_gestosci = GatunekUzytkownikaForm(
            request.POST, instance=rekord)

        if formularz_gestosci.is_valid():
            formularz_gestosci.save(update_fields=['informacje_dodatkowe', ])
            return redirect("uzytkownik:gatunek-detail", slug=slug)

        context = {
            "formularz_gestosci": GatunekUzytkownikaForm(instance=rekord),
        }
        return render(request, "uzytkownik/edytuj_wpis.html", context)


class NowyWpisUzytkownikaView(View):
    """
    Creates a new user's record
    """

    def get(self, request):
        context = {
            "formularz_gestosci": GatunekUzytkownikaForm(),
        }
        return render(request, "uzytkownik/nowy_wpis.html", context)

    def post(self, request):
        formularz_gestosci = GatunekUzytkownikaForm(request.POST)

        if formularz_gestosci.is_valid():
            formularz = formularz_gestosci.save(commit=False)
            formularz.stworzony_przez = request.user
            formularz_gestosci.save()
            return HttpResponseRedirect(reverse("uzytkownik:profil"))

        context = {
            "formularz_gestosci": GatunekUzytkownikaForm(),
        }
        return render(request, "uzytkownik/nowy_wpis.html", context)
