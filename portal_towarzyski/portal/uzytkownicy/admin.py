from django.contrib import admin

# Register your models here.
from .models import Zainteresowania
admin.site.register(Zainteresowania)

from .models import Dane_uzytkownika
admin.site.register(Dane_uzytkownika)

from .models import Znajomi
admin.site.register(Znajomi)

from .models import Znajomi_has_zainteresowania_uzytkownik
admin.site.register(Znajomi_has_zainteresowania_uzytkownik)
