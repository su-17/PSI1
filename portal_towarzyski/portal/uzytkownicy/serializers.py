from django.contrib.auth.models import User

from .models import Zainteresowania, Dane_uzytkownika, Znajomi, Znajomi_has_zainteresowania_uzytkownik
from rest_framework import serializers

class ZainteresowaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zainteresowania
        fields = '__all__'

class Dane_uzytkownikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dane_uzytkownika
        fields = '__all__'
class ZnajomiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Znajomi
        fields = '__all__'
class Znajomi_has_zainteresowania_uzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Znajomi_has_zainteresowania_uzytkownik
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
