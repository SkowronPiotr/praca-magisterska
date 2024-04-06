from django import forms
from django.utils.text import slugify
from uzytkownik.models import GatunekUzytkownika


class GatunekUzytkownikaForm(forms.ModelForm):

    class Meta:
        model = GatunekUzytkownika
        exclude = ['stworzony_przez', 'slug']
        labels = {
            "gestosc": "Podaj gęstość swojego materiału",
            "Aluminum": "Zawartość Aluminium",
            "Boron": "Zawartość Boru",
            "Carbon": "Zawartość Węgla",
            "Chromium": "Zawartość Chromu",
            "Copper": "Zawartość Miedzi",
            "Cobalt": "Zawartość Kobaltu",
            "Iron": "Zawartość Żelaza",
            "Manganese": "Zawartość Manganu",
            "Nickel": "Zawartość Niklu",
            "Phosphorus": "Zawartość Fosforu",
            "Silicon": "Zawartość Krzemu",
            "Vanadium": "Zawartość Wanadu",
            "Tungsten": "Zawartość Wolframu",
            "Molybdenum": "Zawartość Molibdenu",
            "Niobium": "Zawartość Niobu",
            "Titanium": "Zawartość Tytanu",
            "Sulfur": "Zawartość Siarki",
            "Zirconium": "Zawartość Cyrkonu",
            "TensileStrengthUltimate": "Teoretyczna wytrzymałość na rozciąganie [MPa]",
            "TensileStrengthYield": "Rzeczywista wytrzymałość na rozciąganie [MPa]",
            "ElongationAtBreak": "Wydłużenie",
            "ModulusOfElasticity": "Moduł sprężystości",
            "ReductionOfArea": "Redukcja powierzchni",
            "HardnessRockwellB": "Twardość metodą Rockwella",
            "HardnessBrinell": "Twardość metodą Brinella",
            "HardnessKnoop": "Twardość metodą Knoppa",
        }
