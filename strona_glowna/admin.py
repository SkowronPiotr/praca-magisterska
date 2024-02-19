from django.contrib import admin
from .models import DaneWlasciwosciMechanicznych, DaneWlasciwosciFizycznych, DaneSkladuChemicznego, Komentarze, Gatunek, Kategorie
from uzytkownik.models import GatunekUzytkownika


class GatunekUzytkownikaAdmin(admin.ModelAdmin):
    list_filter = ()
   # list_display = ("nazwa", "kategoria")
    list_display = ("nazwa", "stworzony_przez")
    prepopulated_fields = {"slug": ("nazwa",)}


admin.site.register(DaneSkladuChemicznego)
admin.site.register(DaneWlasciwosciFizycznych)
admin.site.register(DaneWlasciwosciMechanicznych)
admin.site.register(Kategorie)
admin.site.register(Komentarze)
admin.site.register(Gatunek)
admin.site.register(GatunekUzytkownika, GatunekUzytkownikaAdmin)
