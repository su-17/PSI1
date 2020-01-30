from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

class ZainteresowaniaList(generics.ListCreateAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Zainteresowania.objects.all()
   serializer_class = ZainteresowaniaSerializer
   def get(self, request, format=None):
      Zainteresowanie = Zainteresowania.objects.all()
      serializer = ZainteresowaniaSerializer(Zainteresowanie,many=True)
      return Response(serializer.data)
   def post(self, request, format=None):
      serializer = ZainteresowaniaSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ZainteresowaniaDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Zainteresowania.objects.all()
   serializer_class = ZainteresowaniaSerializer


class Dane_uzytkownikaList(generics.ListCreateAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Dane_uzytkownika.objects.all()
   serializer_class = Dane_uzytkownikaSerializer
   def get(self, request, format=None):
      uzytkownik = Dane_uzytkownika.objects.all()
      serializer = Dane_uzytkownikaSerializer(uzytkownik,many=True)
      return Response(serializer.data)
   def post(self, request, format=None):
      serializer = Dane_uzytkownikaSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Dane_uzytkownikaDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Dane_uzytkownika.objects.all()
   serializer_class = Dane_uzytkownikaSerializer



class ZnajomiList(generics.ListCreateAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Znajomi.objects.all()
   serializer_class = ZnajomiSerializer
   def get(self, request, format=None):
      znajomy = Znajomi.objects.all()
      serializer = ZnajomiSerializer(znajomy,many=True)
      return Response(serializer.data)
   def post(self, request, format=None):
      serializer = ZnajomiSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ZnajomiDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Znajomi.objects.all()
   serializer_class = ZnajomiSerializer



class Znajomi_has_zainteresowania_uzytkownikList(generics.ListCreateAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Znajomi_has_zainteresowania_uzytkownik.objects.all()
   serializer_class = Znajomi_has_zainteresowania_uzytkownikSerializer
   def get(self, request, format=None):
      znajom = Znajomi_has_zainteresowania_uzytkownik.objects.all()
      serializer = Znajomi_has_zainteresowania_uzytkownikSerializer(znajom,many=True)
      return Response(serializer.data)
   def post(self, request, format=None):
      serializer = Znajomi_has_zainteresowania_uzytkownikSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Znajomi_has_zainteresowania_uzytkownikDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   queryset = Znajomi_has_zainteresowania_uzytkownik.objects.all()
   serializer_class = Znajomi_has_zainteresowania_uzytkownikSerializer


class UserList(generics.ListAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer


def index(request):
   num_zainteresowania = Zainteresowania.objects.all().count()
   num_dane = Dane_uzytkownika.objects.count()
   num_znajomi = Znajomi.objects.count()

   context = {
      'num_zainteresowania': num_zainteresowania,
      'num_dane': num_dane,
      'num_znajomi': num_znajomi,
   }
   return render(request, 'index.html', context=context)