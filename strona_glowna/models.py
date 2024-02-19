from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class DaneWlasciwosciMechanicznych(models.Model):
    Id_właściwości_mechanicznych = models.AutoField(primary_key=True)
    TensileStrengthUltimate = models.FloatField(blank=True, null=True)
    TensileStrengthUltimateUnit = models.CharField(
        max_length=10, blank=True, null=True)

    TensileStrengthYield = models.FloatField(blank=True, null=True)
    TensileStrengthYieldUnit = models.CharField(
        max_length=10, blank=True, null=True)

    ElongationAtBreak = models.FloatField(blank=True, null=True)
    ElongationAtBreakUnit = models.CharField(
        max_length=10, blank=True, null=True)

    ModulusOfElasticity = models.FloatField(blank=True, null=True)
    ModulusOfElasticityUnit = models.CharField(
        max_length=10, blank=True, null=True)

    ReductionOfArea = models.FloatField(blank=True, null=True)
    ReductionOfAreaUnit = models.CharField(
        max_length=10, blank=True, null=True)

    HardnessRockwellB = models.FloatField(blank=True, null=True)

    HardnessBrinell = models.FloatField(blank=True, null=True)
    HardnessBrinellUnit = models.CharField(
        max_length=10, blank=True, null=True)

    HardnessKnoop = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Właściwości mechaniczne"

    def __str__(self):
        return f"{self.Id_właściwości_mechanicznych}"

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


class DaneWlasciwosciFizycznych(models.Model):
    Id_właściwości_fizycznych = models.AutoField(primary_key=True)
    Density = models.FloatField()
    DensityUnit = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Właściwości fizyczne"

    def __str__(self):
        return f"{self.Id_właściwości_fizycznych}"


class DaneSkladuChemicznego(models.Model):
    Id_składu_chemicznego = models.AutoField(primary_key=True)
    Aluminum = models.CharField(max_length=20, blank=True, null=True)
    Boron = models.CharField(max_length=20, blank=True, null=True)
    Carbon = models.CharField(max_length=20, blank=True, null=True)
    Chromium = models.CharField(max_length=20, blank=True, null=True)
    Copper = models.CharField(max_length=20, blank=True, null=True)
    Cobalt = models.CharField(max_length=20, blank=True, null=True)
    Iron = models.CharField(max_length=20, blank=True, null=True)
    Manganese = models.CharField(max_length=20, blank=True, null=True)
    Nickel = models.CharField(max_length=20, blank=True, null=True)
    Phosphorus = models.CharField(max_length=20, blank=True, null=True)
    Silicon = models.CharField(max_length=20, blank=True, null=True)
    Vanadium = models.CharField(max_length=20, blank=True, null=True)
    Tungsten = models.CharField(max_length=20, blank=True, null=True)
    Molybdenum = models.CharField(max_length=20, blank=True, null=True)
    Niobium = models.CharField(max_length=20, blank=True, null=True)
    Titanium = models.CharField(max_length=20, blank=True, null=True)
    Sulfur = models.CharField(max_length=20, blank=True, null=True)
    Zirconium = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Skład chemiczny"

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

    def __str__(self):
        return f"{self.Id_składu_chemicznego}"


class Komentarze(models.Model):
    Id_komentarza = models.AutoField(primary_key=True)
    Komentarz = models.TextField(null=True)
    Aplikacje = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Komentarze"

    def __str__(self):
        return f"{self.Id_komentarza}"


class Kategorie(models.Model):
    nazwa = models.CharField(max_length=255)

    class Meta:
        ordering = ("nazwa",)
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.nazwa


class Gatunek(models.Model):
    kategoria = models.ForeignKey(
        Kategorie, related_name='gatunki', on_delete=models.CASCADE, null=True, blank=True)
    Id_gatunku = models.AutoField(primary_key=True)
    gatunek = models.CharField(max_length=255)
    Id_właściwości_mechanicznych = models.ForeignKey(
        DaneWlasciwosciMechanicznych, on_delete=models.CASCADE)
    Id_właściwości_fizycznych = models.ForeignKey(
        DaneWlasciwosciFizycznych, on_delete=models.CASCADE)
    Id_składu_chemicznego = models.ForeignKey(
        DaneSkladuChemicznego, on_delete=models.CASCADE)
    Id_komentarza = models.ForeignKey(
        Komentarze, on_delete=models.CASCADE, null=True, blank=True)
    stworzony_przez = models.ForeignKey(
        User, related_name="stworzone_gatunki", on_delete=models.CASCADE, default=User.objects.get(username='admin1').pk)

    class Meta:
        verbose_name_plural = "Gatunki"

    def __str__(self):
        return f"{self.gatunek}"
