from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('ZainteresowaniaList/', ZainteresowaniaList.as_view()),
    path('ZainteresowaniaDetails/<int:pk>', ZainteresowaniaDetail.as_view()),

    path('Dane_uzytkownikaList/', Dane_uzytkownikaList.as_view()),
    path('Dane_uzytkownikaDetail/<int:pk>', Dane_uzytkownikaDetail.as_view()),

    path('ZnajomiList/', ZnajomiList.as_view()),
    path('ZnajomiDetails/<int:pk>/', ZnajomiDetail.as_view()),

    path('Znajomi_has_zainteresowania_uzytkownikList/', Znajomi_has_zainteresowania_uzytkownikList.as_view()),
    path('Znajomi_has_zainteresowania_uzytkownikDetails/<int:pk>/', Znajomi_has_zainteresowania_uzytkownikDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]