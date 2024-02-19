from django.urls import reverse
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from strona_glowna.models import Kategorie


class GatunekUzytkownika(models.Model):
    # kategoria = models.CharField(max_length=255, null=True, blank=True)
    kategoria = models.ForeignKey(
        Kategorie, related_name='gatunki_uzytkownika', on_delete=models.CASCADE, null=True, blank=True)
    nazwa = models.CharField(max_length=255)
    gestosc = models.FloatField()
    Aluminum = models.CharField(max_length=20, null=True, blank=True)
    Boron = models.CharField(max_length=20, null=True, blank=True)
    Carbon = models.CharField(max_length=20, null=True, blank=True)
    Chromium = models.CharField(max_length=20, null=True, blank=True)
    Copper = models.CharField(max_length=20, null=True, blank=True)
    Cobalt = models.CharField(max_length=20, null=True, blank=True)
    Iron = models.CharField(max_length=20, null=True, blank=True)
    Manganese = models.CharField(max_length=20, null=True, blank=True)
    Nickel = models.CharField(max_length=20, null=True, blank=True)
    Phosphorus = models.CharField(max_length=20, null=True, blank=True)
    Silicon = models.CharField(max_length=20, null=True, blank=True)
    Vanadium = models.CharField(max_length=20, null=True, blank=True)
    Tungsten = models.CharField(max_length=20, null=True, blank=True)
    Molybdenum = models.CharField(max_length=20, null=True, blank=True)
    Niobium = models.CharField(max_length=20, null=True, blank=True)
    Titanium = models.CharField(max_length=20, null=True, blank=True)
    Sulfur = models.CharField(max_length=20, null=True, blank=True)
    Zirconium = models.CharField(max_length=20, null=True, blank=True)
    informacje_dodatkowe = models.TextField(
        max_length=500, null=True, blank=True)
    TensileStrengthUltimate = models.FloatField(null=True, blank=True)
    TensileStrengthYield = models.FloatField(null=True, blank=True)
    ElongationAtBreak = models.FloatField(null=True, blank=True)
    ModulusOfElasticity = models.FloatField(null=True, blank=True)
    ReductionOfArea = models.FloatField(null=True, blank=True)
    HardnessRockwellB = models.FloatField(null=True, blank=True)
    HardnessBrinell = models.FloatField(null=True, blank=True)
    HardnessKnoop = models.FloatField(null=True, blank=True)
    stworzony_przez = models.ForeignKey(
        User, related_name="stworzone_gatunki_uzytkownika", on_delete=models.CASCADE)
    slug = models.SlugField(default="", null=False,
                            db_index=True, unique=True)

    class Meta:
        verbose_name_plural = "Gatunek Użytkownika"

    def to_dict_sklad_chemiczny(self):
        return {
            "Aluminum": self.Aluminum,
            "Boron": self.Boron,
            "Carbon": self.Carbon,
            "Chromium": self.Chromium,
            "Cobalt": self.Cobalt,
            "Copper": self.Copper,
            "Iron": self.Iron,
            "Manganese": self.Manganese,
            "Molybdenum": self.Molybdenum,
            "Nickel": self.Nickel,
            "Niobium": self.Niobium,
            "Phosphorus": self.Phosphorus,
            "Silicon": self.Silicon,
            "Vanadium": self.Vanadium,
            "Titanium": self.Titanium,
            "Tungsten": self.Tungsten,
            "Sulfur": self.Sulfur,
            "Zirconium": self.Zirconium,
        }

    def to_dict_mechaniczne(self):
        return {
            "TensileStrengthUltimate": self.TensileStrengthUltimate,
            "TensileStrengthYield": self.TensileStrengthYield,
            "ElongationAtBreak": self.ElongationAtBreak,
            "ModulusOfElasticity": self.ModulusOfElasticity,
            "ReductionOfArea": self.ReductionOfArea,
            "HardnessRockwellB": self.HardnessRockwellB,
            "HardnessBrinell": self.HardnessBrinell,
        }

    def get_absolute_url(self):
        return reverse("gatunek_uzytkownika_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nazwa)
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # Jeśli slug nie jest ustawiony, generuj go na podstawie pola nazwa
    #     if not self.slug:
    #         self.slug = slugify(self.nazwa)

    #     # Sprawdź, które pola mają być zapisane
    #     update_fields = kwargs.get('update_fields', None)

    #     if update_fields is None or 'nazwa' in update_fields or 'opis' in update_fields:
    #         # Zapisz tylko wybrane pola
    #         super(GatunekUzytkownika, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nazwa}"
