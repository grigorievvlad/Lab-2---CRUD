from django.contrib import admin

from .models import (
    Clienti,
    DoljnostiCotrudnikov,
    Cotrudniki,
    KategoriTovarov,
    Tovar,
    KategoriiPostavchikov,
    Postavchik,
    Zakazi
)

admin.site.register(Clienti)
admin.site.register(DoljnostiCotrudnikov)
admin.site.register(Cotrudniki)
admin.site.register(KategoriTovarov)
admin.site.register(Tovar)
admin.site.register(KategoriiPostavchikov)
admin.site.register(Postavchik)
admin.site.register(Zakazi)