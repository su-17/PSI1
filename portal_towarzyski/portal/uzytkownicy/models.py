# Create your models here.
from django.db import models
class Zainteresowania(models.Model):
    ID_zainteresowania = models.IntegerField(primary_key=True)
    Zainteresowanie = models.CharField(max_length=45)
    ID_uzytkownika = models.IntegerField()
class Dane_uzytkownika(models.Model):
    ID_uzytkownika = models.IntegerField(primary_key=True)
    Imie_uzytkownika = models.CharField(max_length=45)
    Nazwisko_uzytkownika = models.CharField(max_length=45)
    Wiek = models.IntegerField()
    Miejscowosc = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    Zainteresowania_ID_zainteresowania = models.ForeignKey(Zainteresowania, on_delete=models.CASCADE)
class Znajomi(models.Model):
    ID_znajomego = models.IntegerField(primary_key=True)
    Zainteresowania = models.CharField(max_length=45)
    Wiek = models.IntegerField()
    Miejscowosc = models.CharField(max_length=45)
class Znajomi_has_zainteresowania_uzytkownik(models.Model):
    Znajomi_ID_znajomego = models.ForeignKey(Znajomi, on_delete=models.CASCADE)
    Zainteresowania_uzytkownika_ID_zainteresowania = models.ForeignKey(Zainteresowania, on_delete=models.CASCADE)